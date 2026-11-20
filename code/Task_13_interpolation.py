"""Task 13 - Interpolation. Parameter change = hide the 11:00 reading and see how well we recover it."""
import numpy as np
from scipy.interpolate import interp1d, CubicSpline
import matplotlib.pyplot as plt
from pathlib import Path
FIG = Path(__file__).resolve().parent.parent / "figures"

hours = np.array([8, 9, 10, 11, 12, 13, 14], dtype=float)
temperature = np.array([18.0, 20.0, 22.5, 24.0, 25.0, 25.5, 25.0])
linear, cubic = interp1d(hours, temperature), CubicSpline(hours, temperature)
t10 = np.arange(8, 14 + 1/6, 1/6)
print(f"Linear estimate at 10:30: {float(linear(10.5)):.2f} C")
print(f"Cubic estimate at 10:30: {float(cubic(10.5)):.2f} C")

print("\n--- Parameter change: remove the 11:00 reading (true value 24.0) ---")
mask = hours != 11
lin2, cub2 = interp1d(hours[mask], temperature[mask]), CubicSpline(hours[mask], temperature[mask])
print(f"Linear estimate at 11:00: {float(lin2(11)):.3f} C  (error {abs(float(lin2(11))-24):.3f})")
print(f"Cubic  estimate at 11:00: {float(cub2(11)):.3f} C  (error {abs(float(cub2(11))-24):.3f})")

plt.scatter(hours, temperature, label="Hourly measurements")
plt.plot(t10, linear(t10), label="Linear"); plt.plot(t10, cubic(t10), label="Cubic spline")
plt.xlabel("Hour of day"); plt.ylabel("Temperature (C)"); plt.title("Temperature interpolation")
plt.legend(); plt.grid(True); plt.savefig(FIG / "task_13_original.png", dpi=130, bbox_inches="tight"); plt.show()
