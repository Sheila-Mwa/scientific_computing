"""Task 15 - Numerical differentiation. Parameter change = step size h on a function with a known derivative."""
import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path
FIG = Path(__file__).resolve().parent.parent / "figures"

time = np.arange(7, dtype=float)
position = np.array([0.0, 4.8, 10.2, 16.1, 22.7, 30.0, 38.0])
speed = np.zeros_like(position)
speed[0] = (position[1]-position[0]) / (time[1]-time[0])
for i in range(1, len(time)-1):
    speed[i] = (position[i+1]-position[i-1]) / (time[i+1]-time[i-1])
speed[-1] = (position[-1]-position[-2]) / (time[-1]-time[-2])
for t, x, v in zip(time, position, speed):
    print(f"t={t:.0f}s, position={x:.1f}m, estimated speed={v:.2f}m/s")

print("\n--- Parameter change: step size h for f(x)=sin(x) at x=1 (exact derivative cos(1)) ---")
exact = np.cos(1.0)
hs = 10.0 ** -np.arange(1, 16)
fwd = np.abs((np.sin(1+hs) - np.sin(1)) / hs - exact)
cen = np.abs((np.sin(1+hs) - np.sin(1-hs)) / (2*hs) - exact)
for h, e1, e2 in list(zip(hs, fwd, cen))[::2]:
    print(f"h={h:.0e}  forward error={e1:.2e}  central error={e2:.2e}")
print(f"Best forward h ~ {hs[np.argmin(fwd)]:.0e}, best central h ~ {hs[np.argmin(cen)]:.0e}")

plt.plot(time, speed, marker="o"); plt.xlabel("Time (s)"); plt.ylabel("Estimated speed (m/s)")
plt.title("Speed estimated from GPS position data"); plt.grid(True)
plt.savefig(FIG / "task_15_original.png", dpi=130, bbox_inches="tight"); plt.show()
plt.figure(); plt.loglog(hs, fwd, "o-", label="Forward"); plt.loglog(hs, cen, "s-", label="Central")
plt.xlabel("h"); plt.ylabel("Absolute error"); plt.title("Error vs step size"); plt.legend(); plt.grid(True)
plt.savefig(FIG / "task_15_step_size.png", dpi=130, bbox_inches="tight"); plt.show()
