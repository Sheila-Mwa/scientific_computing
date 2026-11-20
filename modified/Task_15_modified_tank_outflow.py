"""Task 15 (modified): how fast is a water tank emptying? Rate of change from level readings every 10 minutes.
Assumptions: SYNTHETIC readings from L(t) = 3000 - 6t - 0.03t^2 - 0.0004t^3 litres (+/-3 L sensor noise when stated)."""
import numpy as np

rng = np.random.default_rng(5)
t = np.arange(0, 121, 10, dtype=float)                           # minutes
L = lambda t: 3000 - 6*t - 0.03*t**2 - 0.0004*t**3
true_rate = -6 - 0.06*t - 0.0012*t**2                            # exact derivative, L/min

def estimates(level):
    i = np.arange(2, len(t) - 2)                                  # points where all three methods are defined
    forward = (level[i+1] - level[i]) / 10
    central10 = (level[i+1] - level[i-1]) / 20
    central20 = (level[i+2] - level[i-2]) / 40
    return i, forward, central10, central20

def report(level, label):
    i, f, c10, c20 = estimates(level)
    err = lambda e: np.mean(np.abs(e - true_rate[i]))
    print(f"{label:28s} forward h=10: {err(f):.3f} | central h=10: {err(c10):.3f} | central h=20: {err(c20):.3f}  (mean abs error, L/min)")
    return i, c10

report(L(t), "No noise")
noisy = L(t) + rng.normal(0, 3, t.size)
i, c10 = report(noisy, "With +/-3 L sensor noise")
print("\n t(min)  true  central h=10 (noisy data)")
for j, v in zip(i, c10): print(f" {t[j]:5.0f} {true_rate[j]:7.2f} {v:9.2f}")
print(f"\nAt t=60 min the tank loses about {-true_rate[6]:.1f} L/min; at t=110 min about {-true_rate[11]:.1f} L/min (the made-up outflow grows over time).")
