"""Task 13 (modified): average vehicle speed on a busy highway, hourly readings 05:00-12:00.
Assumptions: ILLUSTRATIVE numbers (km/h). Which interpolator recovers hidden readings best?"""
import numpy as np
from scipy.interpolate import interp1d, CubicSpline, PchipInterpolator
import matplotlib.pyplot as plt
from pathlib import Path
FIG = Path(__file__).resolve().parent.parent / "figures"

hours = np.arange(5, 13, dtype=float)
speed = np.array([62, 50, 30, 19, 17, 28, 41, 52], dtype=float)
methods = {"linear": lambda x, y: interp1d(x, y), "cubic spline": lambda x, y: CubicSpline(x, y), "PCHIP": lambda x, y: PchipInterpolator(x, y)}

for t in (7.5, 17/2, 9.25):
    print(f"Speed at {int(t)}:{int((t%1)*60):02d} ->", {k: round(float(m(hours, speed)(t)), 1) for k, m in methods.items()})

print("\nLeave-one-out test (hide one interior reading, predict it):")
errors = {k: [] for k in methods}
for i in range(1, len(hours)-1):
    keep = np.arange(len(hours)) != i
    for k, m in methods.items(): errors[k].append(abs(float(m(hours[keep], speed[keep])(hours[i])) - speed[i]))
for k, e in errors.items(): print(f"  {k:13s} mean error {np.mean(e):.2f} km/h | worst {np.max(e):.2f} km/h")

fine = np.linspace(5, 12, 200)
plt.scatter(hours, speed, color="k", zorder=3, label="Hourly readings")
for k, m in methods.items(): plt.plot(fine, m(hours, speed)(fine), label=k)
plt.xlabel("Hour of day"); plt.ylabel("Average speed (km/h)"); plt.title("Interpolating traffic speed"); plt.legend(); plt.grid(True)
plt.savefig(FIG / "task_13_modified.png", dpi=130, bbox_inches="tight"); plt.show()
