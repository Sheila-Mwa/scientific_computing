"""Task 6 - Ax = b for two server types. Parameter change = different observed totals."""
import numpy as np

A = np.array([[4., 2.], [8., 12.]])      # rows: CPU, memory; columns: Type A, Type B

for label, b in (("Original totals (20 CPU, 72 GB)", [20., 72.]),
                 ("Changed totals  (22 CPU, 72 GB)", [22., 72.])):
    b = np.array(b)
    x = np.linalg.solve(A, b)
    residual = b - A @ x
    print(label)
    print("  Type A, Type B servers:", x)
    print("  A @ x:", A @ x, "| residual norm:", np.linalg.norm(residual))
print("Condition number of A:", round(np.linalg.cond(A), 3))
