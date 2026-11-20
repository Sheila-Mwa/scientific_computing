"""Task 10 - Bisection and fixed point. Parameter change = stronger heat source (10 -> 300)."""
import numpy as np
from scipy.optimize import root_scalar
import matplotlib.pyplot as plt
from pathlib import Path
FIG = Path(__file__).resolve().parent.parent / "figures"

def make(c):
    f = lambda T: T - 25 - c*np.exp(-T/20)       # heat balance
    g = lambda T: 25 + c*np.exp(-T/20)           # fixed-point form T = g(T)
    return f, g

def fixed_point(g, T0, tol=1e-10, n=100):
    hist = [T0]
    for _ in range(n):
        T_new = g(hist[-1]); hist.append(T_new)
        if abs(T_new - hist[-2]) < tol: break
    return hist

f, g = make(10)
sol = root_scalar(f, bracket=[20, 40], method="bisect", xtol=1e-10)
hist = fixed_point(g, 30.0)
print(f"[c=10]  Bisection: {sol.root:.6f} C ({sol.iterations} iterations) | Fixed-point: {hist[-1]:.6f} C ({len(hist)-1} iterations)")

print("\n--- Parameter change: c = 300 ---")
f3, g3 = make(300)
sol3 = root_scalar(f3, bracket=[20, 80], method="bisect", xtol=1e-10)
hist3 = fixed_point(g3, 40.0, n=15)
print(f"[c=300] Bisection: {sol3.root:.6f} C ({sol3.iterations} iterations)")
print("[c=300] Fixed-point iterates:", np.round(hist3[:10], 2), "... (does not settle)")
print("|g'(root)| for c=10 :", round(10/20*np.exp(-sol.root/20), 3), "| for c=300:", round(300/20*np.exp(-sol3.root/20), 3))

temps = np.linspace(20, 40, 300)
plt.plot(temps, f(temps)); plt.axhline(0, lw=0.8); plt.axvline(sol.root, ls="--")
plt.xlabel("Temperature (C)"); plt.ylabel("Heat-balance function"); plt.title("Equilibrium temperature")
plt.grid(True); plt.savefig(FIG / "task_10_original.png", dpi=130, bbox_inches="tight"); plt.show()
