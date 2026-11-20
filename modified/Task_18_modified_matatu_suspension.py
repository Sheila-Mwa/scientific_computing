"""Task 18 (modified): a matatu wheel after a speed bump - mass-spring-damper, solved with solve_ivp.
Model (quarter vehicle): m y'' + c y' + k y = 0, y = body displacement (m).
Assumptions: m = 450 kg, k = 30,000 N/m, starts 0.08 m above rest with zero velocity.
Three shock absorbers: worn (c=500), healthy (c=2500), stiff (c=7000) N s/m."""
import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt
from pathlib import Path
FIG = Path(__file__).resolve().parent.parent / "figures"

m, k = 450.0, 30000.0
c_crit = 2*np.sqrt(k*m)
print(f"Natural frequency {np.sqrt(k/m)/(2*np.pi):.2f} Hz | critical damping c = {c_crit:.0f} N s/m")

def simulate(c):
    f = lambda t, s: [s[1], -(c*s[1] + k*s[0]) / m]               # s = [y, y']
    return solve_ivp(f, (0, 10), [0.08, 0.0], t_eval=np.linspace(0, 10, 2000), rtol=1e-9, atol=1e-12)

for name, c in (("worn", 500.0), ("healthy", 2500.0), ("stiff", 7000.0)):
    s = simulate(c); y = s.y[0]
    zeta = c / c_crit
    outside = np.flatnonzero(np.abs(y) > 0.02*0.08)               # 2 % of the starting height
    settle = s.t[outside[-1]] if outside.size else 0.0
    big = y[np.abs(y) > 0.02*0.08]                                  # ignore the invisible tiny wiggles
    crossings = int(np.sum(np.diff(np.sign(big)) != 0))
    print(f"{name:8s} c={c:>6.0f} damping ratio {zeta:.2f} | settles (2%) after {settle:.2f} s | zero-crossings {crossings} | lowest point {y.min()*100:.2f} cm")
    plt.plot(s.t, y*100, label=f"{name} (zeta={zeta:.2f})")
plt.axhline(0, color="k", lw=0.6); plt.xlabel("Time (s)"); plt.ylabel("Body displacement (cm)")
plt.title("Matatu body motion after a speed bump"); plt.xlim(0, 5); plt.legend(); plt.grid(True)
plt.savefig(FIG / "task_18_modified.png", dpi=130, bbox_inches="tight"); plt.show()
