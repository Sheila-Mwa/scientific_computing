"""Task 20 - Monte Carlo overload probability. Parameter change = demand spread, mean and N."""
import numpy as np
from scipy.stats import norm
import matplotlib.pyplot as plt
from pathlib import Path
FIG = Path(__file__).resolve().parent.parent / "figures"

def simulate(capacity, mean, std, N, seed=42):
    demand = np.random.default_rng(seed).normal(mean, std, N)
    over = demand > capacity
    return over, over.mean(), norm.sf(capacity, mean, std)

over, p, exact = simulate(1000, 850, 120, 100_000)
print(f"Original: estimated {p:.4%} | exact (normal tail) {exact:.4%} | {over.sum()} of 100000")
cases = {"std 120 -> 200": (1000, 850, 200, 100_000, 42),
         "mean 850 -> 900": (1000, 900, 120, 100_000, 42),
         "N = 1,000 (seed 42)": (1000, 850, 120, 1_000, 42),
         "N = 1,000 (seed 7)": (1000, 850, 120, 1_000, 7)}
for label, (cap, mu, sd, n, seed) in cases.items():
    _, p2, e2 = simulate(cap, mu, sd, n, seed)
    print(f"{label:22s}: estimated {p2:.4%} | exact {e2:.4%}")

N = 100_000
running = np.cumsum(over) / np.arange(1, N+1)
idx = np.unique(np.logspace(1, np.log10(N), 200).astype(int)) - 1
plt.semilogx(idx+1, running[idx]); plt.axhline(exact, ls="--", color="gray")
plt.xlabel("Number of simulations"); plt.ylabel("Estimated overload probability")
plt.title("Monte Carlo estimate of server-overload risk"); plt.grid(True)
plt.savefig(FIG / "task_20_original.png", dpi=130, bbox_inches="tight"); plt.show()
