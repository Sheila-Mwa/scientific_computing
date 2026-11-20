"""Task 16 - Numerical integration. Parameter change = fewer, more widely spaced readings."""
import numpy as np
from scipy.integrate import simpson

trap = getattr(np, "trapezoid", None) or np.trapz        # works on old and new NumPy
t = np.array([0, 2, 4, 6, 8, 10, 12], dtype=float)
p = np.array([0.8, 1.0, 1.4, 1.8, 1.6, 1.2, 0.9])

print("Readings every 2 h")
print(f"  Trapezoidal: {trap(p, t):.3f} kWh | Simpson: {simpson(p, x=t):.3f} kWh | difference {abs(simpson(p, x=t)-trap(p, t)):.3f} kWh")
sub = slice(0, None, 3)                                   # every 6 h: t = 0, 6, 12
print("Readings every 6 h (parameter change)")
print(f"  Trapezoidal: {trap(p[sub], t[sub]):.3f} kWh | Simpson: {simpson(p[sub], x=t[sub]):.3f} kWh")
