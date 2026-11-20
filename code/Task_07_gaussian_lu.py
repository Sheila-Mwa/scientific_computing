"""Task 7 - LU decomposition. Parameter change = a nearly singular matrix (ill-conditioning)."""
import numpy as np
from scipy.linalg import lu_factor, lu_solve

A = np.array([[4., -1., 0.], [-1., 4., -1.], [0., -1., 3.]])
sets = [np.array([15., 10., 10.]), np.array([16., 11., 9.]), np.array([14., 12., 11.])]

lu, piv = lu_factor(A)                    # factor ONCE
for i, b in enumerate(sets, 1):
    x = lu_solve((lu, piv), b)
    print(f"Set {i}: x={x}  residual norm={np.linalg.norm(b - A @ x):.2e}")
print("Direct solve, set 1:", np.linalg.solve(A, sets[0]))

print("\n--- Parameter change: diagonal 4,4,3 -> 1.42 (almost singular) ---")
B = np.array([[1.42, -1., 0.], [-1., 1.42, -1.], [0., -1., 1.42]])
b = np.array([15., 10., 10.])
x1 = np.linalg.solve(B, b)
x2 = np.linalg.solve(B, b + np.array([0.01, 0., 0.]))   # tiny change in b
print("Condition number A:", round(np.linalg.cond(A), 2), "| condition number B:", round(np.linalg.cond(B), 1))
print("A: solution shift for b+0.01:", np.linalg.norm(lu_solve((lu, piv), b + np.array([0.01, 0, 0])) - lu_solve((lu, piv), b)))
print("B: solution shift for b+0.01:", np.linalg.norm(x2 - x1))
