"""Task 18 - RC circuit with solve_ivp. Parameter change = resistance R (time constant)."""
import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt
from pathlib import Path
FIG = Path(__file__).resolve().parent.parent / "figures"

Vs, C, V0 = 5.0, 0.001, 0.0
t_eval = np.linspace(0, 5, 200)

def run(R):
    sol = solve_ivp(lambda t, V: [(Vs - V[0]) / (R*C)], (0, 5), [V0], t_eval=t_eval, rtol=1e-9, atol=1e-11)
    exact = Vs * (1 - np.exp(-sol.t / (R*C)))
    return sol, exact

for R in (1000.0, 2000.0, 500.0):
    sol, exact = run(R)
    tau = R*C
    v1 = float(np.interp(1.0, sol.t, sol.y[0]))
    print(f"R={R:>6.0f} ohm tau={tau:.1f}s | V(1 s)={v1:.3f} V | V(5 s)={sol.y[0,-1]:.4f} V | max error {np.max(np.abs(sol.y[0]-exact)):.2e} V")

for R in (500.0, 1000.0, 2000.0):
    s, _ = run(R); plt.plot(s.t, s.y[0], label=f"R={R:.0f} ohm")
plt.xlabel("Time (s)"); plt.ylabel("Capacitor voltage (V)"); plt.title("RC circuit charging")
plt.legend(); plt.grid(True); plt.savefig(FIG / "task_18_original.png", dpi=130, bbox_inches="tight"); plt.show()
