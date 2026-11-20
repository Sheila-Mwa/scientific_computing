"""Task 4 - Floating-point errors. Parameter change = better approximation of sqrt(2) and smaller x."""
import numpy as np

calculated, expected = 0.1 + 0.2, 0.3
print("0.1 + 0.2 =", calculated)
print("Exact comparison:", calculated == expected)
print("Tolerance-based comparison:", np.isclose(calculated, expected))

true_value = np.sqrt(2)
for approx_value in (1.414, 1.41421):          # 1.414 is the handout value
    absolute_error = abs(true_value - approx_value)
    relative_error = absolute_error / abs(true_value)
    print(f"approx={approx_value}: absolute={absolute_error:.8f}, relative={relative_error:.8%}")

print("\nUnstable vs stable formula for (sqrt(1+x)-1)/x")
for x in [1e-4, 1e-8, 1e-12, 1e-16]:           # 1e-16 added by me
    direct = (np.sqrt(1 + x) - 1) / x
    stable = 1 / (np.sqrt(1 + x) + 1)
    print(f"x={x:.0e}: direct={direct:.12f}, stable={stable:.12f}")
