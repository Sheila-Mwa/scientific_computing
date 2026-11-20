"""Task 8 - Jacobi and Gauss-Seidel. Parameter change = tolerance and grid size."""
import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path
FIG = Path(__file__).resolve().parent.parent / "figures"

def build(n):
    A = 2*np.eye(n) - np.eye(n, k=1) - np.eye(n, k=-1)
    b = np.zeros(n); b[0], b[-1] = 100., 20.
    return A, b

def jacobi(A, b, tol=1e-8, max_iter=50000):
    D = np.diag(A); R = A - np.diagflat(D); x = np.zeros_like(b); errors = []
    for _ in range(max_iter):
        x_new = (b - R @ x) / D
        err = np.linalg.norm(x_new - x, ord=np.inf); errors.append(err)
        if err < tol: return x_new, errors
        x = x_new
    return x, errors

def gauss_seidel(A, b, tol=1e-8, max_iter=50000):
    x = np.zeros_like(b); errors = []
    for _ in range(max_iter):
        old = x.copy()
        for i in range(len(b)):
            x[i] = (b[i] - A[i, :i] @ x[:i] - A[i, i+1:] @ old[i+1:]) / A[i, i]
        err = np.linalg.norm(x - old, ord=np.inf); errors.append(err)
        if err < tol: return x, errors
    return x, errors

A, b = build(5)
x_j, err_j = jacobi(A, b); x_gs, err_gs = gauss_seidel(A, b); x_ex = np.linalg.solve(A, b)
print("Jacobi        :", np.round(x_j, 4), f"({len(err_j)} iterations)")
print("Gauss-Seidel  :", np.round(x_gs, 4), f"({len(err_gs)} iterations)")
print("Direct        :", np.round(x_ex, 4))

print("\n--- Parameter change 1: looser tolerance 1e-3 ---")
print("Jacobi iterations:", len(jacobi(A, b, tol=1e-3)[1]), "| Gauss-Seidel iterations:", len(gauss_seidel(A, b, tol=1e-3)[1]))
print("\n--- Parameter change 2: more grid points ---")
for n in (5, 10, 20, 40):
    A2, b2 = build(n)
    print(f"n={n:>2}: Jacobi {len(jacobi(A2, b2)[1]):>5} iterations, Gauss-Seidel {len(gauss_seidel(A2, b2)[1]):>5} iterations")

plt.semilogy(err_j, label="Jacobi"); plt.semilogy(err_gs, label="Gauss-Seidel")
plt.xlabel("Iteration"); plt.ylabel("Maximum change"); plt.title("Convergence of iterative temperature solution")
plt.legend(); plt.grid(True); plt.savefig(FIG / "task_08_original.png", dpi=130, bbox_inches="tight"); plt.show()
