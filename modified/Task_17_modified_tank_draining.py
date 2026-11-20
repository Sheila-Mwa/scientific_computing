"""Task 17 (modified): a tank draining through a hole - Torricelli's law dh/dt = -k sqrt(h).
Assumptions: h0 = 2.5 m, k = 0.04 m^0.5 per minute. Exact: sqrt(h) = sqrt(h0) - k t/2, empty at t = 2 sqrt(h0)/k."""
import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path
FIG = Path(__file__).resolve().parent.parent / "figures"

h0, k = 2.5, 0.04
t_empty = 2*np.sqrt(h0)/k
exact = lambda t: np.maximum(np.sqrt(h0) - k*t/2, 0)**2
print(f"Exact time to empty: {t_empty:.2f} minutes")

def euler(step, t_end=60.0):
    t = np.arange(0, t_end + step/2, step); h = np.empty_like(t); h[0] = h0
    for i in range(len(t)-1):
        h[i+1] = max(h[i] + step*(-k*np.sqrt(h[i])), 0.0)       # clip at zero: no negative water
    return t, h

for step in (10.0, 5.0, 1.0, 0.1):
    t, h = euler(step)
    print(f"step {step:>4} min: height at 60 min = {h[-1]:.4f} m | exact {exact(60):.4f} m | error {abs(h[-1]-exact(60)):.4f} m")
t, h = euler(5.0, 80.0)
reached = t[np.argmax(h == 0)] if (h == 0).any() else None
print("Euler (step 5) says the tank is empty at t =", reached, "min")

for step in (10.0, 1.0):
    tt, hh = euler(step, 80); plt.plot(tt, hh, "o-" if step > 2 else "-", ms=4, label=f"Euler step {step:g} min")
tt = np.linspace(0, 80, 400); plt.plot(tt, exact(tt), "k--", label="Exact")
plt.xlabel("Time (min)"); plt.ylabel("Water height (m)"); plt.title("Tank draining: Euler vs exact"); plt.legend(); plt.grid(True)
plt.savefig(FIG / "task_17_modified.png", dpi=130, bbox_inches="tight"); plt.show()
