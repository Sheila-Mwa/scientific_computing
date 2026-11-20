"""Task 5 (modified): re-drawing a farm plot on a rotated, stretched map.
Assumptions: plot corners in metres; map is rotated 25 deg and stretched 1.2 in x, 0.9 in y."""
import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path
FIG = Path(__file__).resolve().parent.parent / "figures"

plot = np.array([[0, 0], [60, 5], [75, 50], [20, 65], [-5, 30]], dtype=float)   # corners, in order

def shoelace(p):
    x, y = p[:, 0], p[:, 1]
    return 0.5 * abs(np.dot(x, np.roll(y, -1)) - np.dot(y, np.roll(x, -1)))

a = np.deg2rad(25)
R = np.array([[np.cos(a), -np.sin(a)], [np.sin(a), np.cos(a)]])
S = np.diag([1.2, 0.9])
M = R @ S
new = plot @ M.T
print("Transformation matrix:\n", np.round(M, 4))
print(f"Area before: {shoelace(plot):.1f} m2 | after: {shoelace(new):.1f} m2")
print(f"|det(M)| = {abs(np.linalg.det(M)):.4f} | area ratio = {shoelace(new)/shoelace(plot):.4f}")
print(f"Inverse check (M^-1 M = I): {np.allclose(np.linalg.inv(M) @ M, np.eye(2))}")
back = new @ np.linalg.inv(M).T
print("Recovered original corners:", np.allclose(back, plot))

for pts, lab in ((plot, "Original plot"), (new, "Transformed plot")):
    closed = np.vstack([pts, pts[0]]); plt.plot(closed[:, 0], closed[:, 1], "o-", label=lab)
plt.axis("equal"); plt.grid(True); plt.legend(); plt.title("Farm plot before and after transformation")
plt.savefig(FIG / "task_05_modified.png", dpi=130, bbox_inches="tight"); plt.show()
