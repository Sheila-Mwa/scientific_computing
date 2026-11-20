"""Task 12 (modified): locate a phone from distances to cell towers (trilateration).
Assumptions: local map in km; towers at (0,0), (6,0), (3,5); measured distances have small errors."""
import numpy as np
from scipy.optimize import root, least_squares

towers = np.array([[0., 0.], [6., 0.], [3., 5.]])
true_pos = np.array([2.0, 3.0])
exact = np.linalg.norm(towers - true_pos, axis=1)
measured = exact + np.array([0.015, -0.02, 0.014])          # small measurement noise (km)
print("Exact distances:", np.round(exact, 4), "| measured:", np.round(measured, 4))

def two_circles(z):
    return [np.hypot(z[0]-towers[0, 0], z[1]-towers[0, 1]) - measured[0],
            np.hypot(z[0]-towers[1, 0], z[1]-towers[1, 1]) - measured[1]]

print("\nTwo towers give TWO candidate positions (two circle intersections):")
cands = []
for guess in ([2., 3.], [2., -3.]):
    s = root(two_circles, guess); cands.append(s.x)
    d3 = np.linalg.norm(s.x - towers[2])
    print(f"  guess {guess} -> {np.round(s.x, 3)} | residual {np.round(two_circles(s.x), 8)} | distance to tower 3 = {d3:.3f} (measured {measured[2]:.3f})")
best = min(cands, key=lambda p: abs(np.linalg.norm(p - towers[2]) - measured[2]))
print("Third tower picks:", np.round(best, 3))

ls = least_squares(lambda z: np.linalg.norm(towers - z, axis=1) - measured, [1., 1.])
print("Using all three towers (least squares):", np.round(ls.x, 3), "| error vs true position:", round(np.linalg.norm(ls.x - true_pos)*1000, 1), "m")
big = measured + np.array([0.3, -0.4, 0.2])
ls2 = least_squares(lambda z: np.linalg.norm(towers - z, axis=1) - big, [1., 1.])
print("With 300-400 m measurement errors:", np.round(ls2.x, 3), "| position error:", round(np.linalg.norm(ls2.x - true_pos)*1000), "m")
