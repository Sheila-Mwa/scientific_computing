"""Task 8 (modified): steady temperature on a 2-D solar drying tray (10 x 10 interior points).
Assumptions: bottom edge heated to 60 C, other three edges at 25 C. Compares Jacobi, Gauss-Seidel and SOR."""
import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path
FIG = Path(__file__).resolve().parent.parent / "figures"

n = 10
N = n*n
A = np.zeros((N, N)); b = np.zeros(N)
idx = lambda i, j: i*n + j                      # i = row (0 = top), j = column
T_top, T_side, T_bottom = 25., 25., 60.
for i in range(n):
    for j in range(n):
        k = idx(i, j); A[k, k] = 4
        for di, dj in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            ii, jj = i+di, j+dj
            if 0 <= ii < n and 0 <= jj < n: A[k, idx(ii, jj)] = -1
            else: b[k] += T_bottom if ii == n else (T_top if ii < 0 else T_side)

def iterate(method, omega=1.0, tol=1e-6, max_iter=20000):
    x = np.zeros(N); errs = []
    D = np.diag(A); R = A - np.diagflat(D)
    for _ in range(max_iter):
        if method == "jacobi":
            new = (b - R @ x) / D
        else:
            new = x.copy()
            for i in range(N):
                gs = (b[i] - A[i, :i] @ new[:i] - A[i, i+1:] @ x[i+1:]) / A[i, i]
                new[i] = (1 - omega)*x[i] + omega*gs
        err = np.max(np.abs(new - x)); errs.append(err); x = new
        if err < tol: break
    return x, errs

exact = np.linalg.solve(A, b)
omega_opt = 2 / (1 + np.sin(np.pi/(n+1)))
results = {"Jacobi": iterate("jacobi"), "Gauss-Seidel": iterate("gs"), f"SOR (w={omega_opt:.2f})": iterate("gs", omega_opt)}
for name, (x, e) in results.items():
    print(f"{name:18s}: {len(e):>4} iterations | max difference from direct solve {np.max(np.abs(x-exact)):.2e}")
grid = exact.reshape(n, n)
print(f"Temperature next to hot edge: {grid[-1].mean():.1f} C | next to top edge: {grid[0].mean():.1f} C | centre: {grid[n//2, n//2]:.1f} C")

fig, ax = plt.subplots(1, 2, figsize=(10, 4))
im = ax[0].imshow(grid, cmap="inferno"); fig.colorbar(im, ax=ax[0], label="C"); ax[0].set_title("Tray temperature (top row = top edge)")
for name, (x, e) in results.items(): ax[1].semilogy(e, label=name)
ax[1].set_xlabel("Iteration"); ax[1].set_ylabel("Max change"); ax[1].legend(); ax[1].grid(True); ax[1].set_title("Convergence")
plt.savefig(FIG / "task_08_modified.png", dpi=130, bbox_inches="tight"); plt.show()
