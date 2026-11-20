"""Task 10 (modified): how deep is the water in a horizontal cylindrical tank holding 4,000 L?
Assumptions: tank length 3.0 m, radius 0.8 m, lying on its side. Volume is NONlinear in depth h:
V(h) = L * ( r^2 * arccos((r-h)/r) - (r-h) * sqrt(2rh - h^2) )."""
import numpy as np
from scipy.optimize import brentq
import matplotlib.pyplot as plt
from pathlib import Path
FIG = Path(__file__).resolve().parent.parent / "figures"

L, r, target_m3 = 3.0, 0.8, 4.0
def volume(h): return L * (r**2*np.arccos((r-h)/r) - (r-h)*np.sqrt(2*r*h - h**2))
f = lambda h: volume(h) - target_m3

def bisection(f, a, b, tol=1e-6):
    log = []
    while (b - a) / 2 > tol:
        m = (a + b) / 2; log.append((a, b, m))
        if f(a) * f(m) <= 0: b = m
        else: a = m
    return (a + b) / 2, log

print(f"Full tank volume: {volume(2*r)*1000:.0f} L (check: pi r^2 L = {np.pi*r*r*L*1000:.0f} L)")
h, log = bisection(f, 1e-9, 2*r - 1e-9)
print(f"Depth for 4000 L: {h:.5f} m  ({h/(2*r):.1%} of the diameter) after {len(log)} halvings")
print(f"Check: volume at that depth = {volume(h)*1000:.3f} L | SciPy brentq gives {brentq(f, 1e-9, 2*r-1e-9):.5f} m")
print("First four bracket intervals:", [(round(a, 3), round(b, 3)) for a, b, _ in log[:4]])
for lit in (1000, 3000, 5000):
    hh, lg = bisection(lambda x: volume(x) - lit/1000, 1e-9, 2*r - 1e-9)
    print(f"  {lit} L -> depth {hh:.4f} m")

hs = np.linspace(0.001, 2*r - 0.001, 200)
plt.plot(hs, volume(hs)*1000); plt.axhline(4000, ls="--"); plt.axvline(h, ls="--")
plt.xlabel("Water depth h (m)"); plt.ylabel("Volume (L)"); plt.title("Horizontal tank: volume vs depth"); plt.grid(True)
plt.savefig(FIG / "task_10_modified.png", dpi=130, bbox_inches="tight"); plt.show()
