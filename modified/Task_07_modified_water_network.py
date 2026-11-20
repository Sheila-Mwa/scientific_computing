"""Task 7 (modified): hourly pressure DROP (below the reservoir level) in a small village water network with LU reuse.
Assumptions: 4 junctions; matrix = pipe conductances (same all day); right-hand side = hourly demand pattern."""
import numpy as np, time
from scipy.linalg import lu_factor, lu_solve

A = np.array([[3., -1., 0., 0.], [-1., 3., -1., 0.], [0., -1., 3., -1.], [0., 0., -1., 2.]])
base = np.array([10., 6., 8., 4.])
hours = np.arange(24)
pattern = 0.4 + 0.6*np.exp(-((hours-7)/2.0)**2) + 0.8*np.exp(-((hours-18)/2.5)**2)   # morning and evening peaks

lu, piv = lu_factor(A)
drops = np.array([lu_solve((lu, piv), base * p) for p in pattern])
print("Peak demand hour:", int(pattern.argmax()), "| pressure drop at junction 1 at peak:", round(drops[pattern.argmax(), 0], 2))
print("Largest pressure drop overall: junction", int(drops.max(axis=0).argmax()) + 1, "value", round(drops.max(), 2))
print("Max residual over all 24 solves:", max(np.linalg.norm(base*p - A @ h) for p, h in zip(pattern, drops)))

# Timing on a bigger network: 400 junctions, 500 demand vectors
n = 400
Big = 2.5*np.eye(n) - np.eye(n, k=1) - np.eye(n, k=-1)
B = np.random.default_rng(0).uniform(1, 10, (n, 500))
t0 = time.perf_counter()
for j in range(500): np.linalg.solve(Big, B[:, j])
t_repeat = time.perf_counter() - t0
t0 = time.perf_counter()
f = lu_factor(Big)
for j in range(500): lu_solve(f, B[:, j])
t_lu = time.perf_counter() - t0
print(f"500 solves of a 400x400 system: repeated solve {t_repeat:.3f}s | LU once + reuse {t_lu:.3f}s | speed-up {t_repeat/t_lu:.1f}x")
