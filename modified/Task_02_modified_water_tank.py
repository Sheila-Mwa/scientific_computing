"""Task 2 (modified): rooftop water tank in an estate with rationed supply.
Assumptions: 5,000 L tank, one reading per hour (illustrative data, not real sensor data)."""
import numpy as np

CAPACITY_L = 5000
level_l = np.array([4200, 4050, 4600, 4900, 5000, 4950, 4700, 4300, 3900, 3600, 3350, 3100,
                    2900, 2700, 2550, 2300, 2050, 1700, 1300, 1000, 850, 700, 950, 1250], dtype=float)

print(f"Mean level: {level_l.mean():.0f} L | min: {level_l.min():.0f} L | max: {level_l.max():.0f} L")
print(f"Mean level in cubic metres: {level_l.mean()/1000:.2f} m3")
percent = level_l / CAPACITY_L * 100
low = np.flatnonzero(percent <= 20)                      # boolean mask -> indices
print("Hours at or below 20% full:", low.tolist())
change = np.diff(level_l)                                # litres gained/lost each hour
print(f"Biggest hourly drop: {change.min():.0f} L between hour {change.argmin()} and {change.argmin()+1}")
print(f"Total water used (sum of drops): {-change[change < 0].sum():.0f} L")
print(f"Total water pumped in (sum of rises): {change[change > 0].sum():.0f} L")
