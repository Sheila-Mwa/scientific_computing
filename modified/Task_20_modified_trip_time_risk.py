"""Task 20 (modified): will I reach an 08:00 class on time? Monte Carlo on matatu travel time.
Assumptions (illustrative): free-flow time 55 min; congestion delay lognormal (median 15 min); number of extra stops
~ Poisson(6) with 2 min exponential delay each; 10 % chance of a breakdown/accident delay uniform 15-45 min."""
import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path
FIG = Path(__file__).resolve().parent.parent / "figures"

def trip_times(N, seed=2026):
    rng = np.random.default_rng(seed)
    congestion = rng.lognormal(np.log(15), 0.5, N)
    stops = rng.poisson(6, N) * rng.exponential(2.0, N)
    incident = (rng.random(N) < 0.10) * rng.uniform(15, 45, N)
    return 55 + congestion + stops + incident

N = 200_000
T = trip_times(N)
print(f"Mean trip {T.mean():.1f} min | median {np.median(T):.1f} | 90th percentile {np.percentile(T, 90):.1f} | 95th {np.percentile(T, 95):.1f}")

depart_to_deadline = lambda leave_min: 480 - leave_min           # 08:00 = 480 min after midnight
for hh, mm in ((6, 0), (6, 20), (6, 40)):
    leave = hh*60 + mm
    p_late = np.mean(T > depart_to_deadline(leave))
    se = np.sqrt(p_late*(1-p_late)/N)
    print(f"Leave {hh:02d}:{mm:02d}: P(late) = {p_late:.2%} (+/- {1.96*se:.2%} at 95% confidence)")

q95 = np.percentile(T, 95)
latest = 480 - q95
print(f"To be late at most 5% of the time, leave by {int(latest//60):02d}:{int(latest%60):02d}")
small = trip_times(500, seed=1)
print(f"Only 500 simulations -> P(late, leave 06:20) = {np.mean(small > 100):.1%} (compare {np.mean(T > 100):.2%} with 200,000)")

plt.hist(T, bins=80, density=True, alpha=0.8); plt.axvline(100, color="r", ls="--", label="Leave 06:20 -> 100 min available")
plt.xlabel("Trip time (min)"); plt.ylabel("Density"); plt.title("Simulated matatu trip times"); plt.legend()
plt.savefig(FIG / "task_20_modified.png", dpi=130, bbox_inches="tight"); plt.show()
