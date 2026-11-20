"""Task 17 - Euler method for cooling. Parameter change = step size h (and a deliberately unstable case)."""
import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path
FIG = Path(__file__).resolve().parent.parent / "figures"

T_amb, T0, end = 25.0, 90.0, 30.0

def euler(k, h):
    time = np.arange(0, end + h/2, h)
    T = np.zeros_like(time); T[0] = T0
    for i in range(len(time)-1):
        T[i+1] = T[i] + h * (-k * (T[i] - T_amb))
    return time, T

exact = lambda t, k: T_amb + (T0 - T_amb) * np.exp(-k*t)
print("k = 0.12")
for h in (5.0, 2.0, 1.0, 0.5, 0.1):
    t, T = euler(0.12, h)
    print(f"  h={h:<4}: Euler {T[-1]:.4f} C | exact {exact(t[-1], 0.12):.4f} C | error {abs(T[-1]-exact(t[-1], 0.12)):.4f}")
t, T = euler(0.5, 5.0)
print("k = 0.5, h = 5 (k*h = 2.5 > 2): first values", np.round(T[:6], 1))

t1, T1 = euler(0.12, 1.0)
plt.plot(t1, T1, "o-", label="Euler h=1"); plt.plot(t1, exact(t1, 0.12), label="Exact")
plt.xlabel("Time (minutes)"); plt.ylabel("Temperature (C)"); plt.title("Cooling of a hot object")
plt.legend(); plt.grid(True); plt.savefig(FIG / "task_17_original.png", dpi=130, bbox_inches="tight"); plt.show()
