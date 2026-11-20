"""Task 2 - NumPy arrays: hourly temperatures.
Part 1 = handout program. Part 2 = my parameter change (a faulty sensor spike)."""
import numpy as np

temperatures_c = np.array([
    18.5, 18.0, 17.8, 17.5, 17.9, 19.0,
    21.5, 23.8, 25.6, 27.1, 28.3, 29.0,
    29.4, 29.1, 28.5, 27.6, 26.2, 24.8,
    23.4, 22.1, 21.0, 20.2, 19.6, 19.0
])

print("=== Part 1: original ===")
mean_temp, min_temp, max_temp = np.mean(temperatures_c), np.min(temperatures_c), np.max(temperatures_c)
temperatures_f = 1.8 * temperatures_c + 32          # vectorized C -> F
print(f"Daily mean temperature: {mean_temp:.2f} C")
print(f"Minimum temperature: {min_temp:.2f} C")
print(f"Maximum temperature: {max_temp:.2f} C")
print("First six Fahrenheit readings:", temperatures_f[:6])

print("\n=== Part 2: parameter change (reading at 12:00 replaced by a 45.0 C spike) ===")
spiked = temperatures_c.copy()
spiked[12] = 45.0
for name, arr in (("original", temperatures_c), ("with spike", spiked)):
    print(f"{name:11s} mean={arr.mean():.2f}  median={np.median(arr):.2f}  max={arr.max():.2f}")
