"""Task 14 (modified): growth of farmed tilapia - logistic S-curve vs a quadratic.
Assumptions: SYNTHETIC data generated from W = 800/(1+exp(-0.30(t-14))) plus random noise (sd 15 g), weeks 0-26."""
import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt
from pathlib import Path
FIG = Path(__file__).resolve().parent.parent / "figures"

rng = np.random.default_rng(11)
weeks = np.arange(0, 27, 2, dtype=float)
weight = 800/(1 + np.exp(-0.30*(weeks - 14))) + rng.normal(0, 15, weeks.size)

logistic = lambda t, Wmax, k, t0: Wmax / (1 + np.exp(-k*(t - t0)))
quad = lambda t, a, b, c: a*t**2 + b*t + c

(p, cov) = curve_fit(logistic, weeks, weight, p0=[700, 0.2, 12])
se = np.sqrt(np.diag(cov))
pred = logistic(weeks, *p)
r2 = 1 - np.sum((weight - pred)**2) / np.sum((weight - weight.mean())**2)
rmse = np.sqrt(np.mean((weight - pred)**2))
print(f"Logistic fit: Wmax = {p[0]:.1f} +/- {se[0]:.1f} g | k = {p[1]:.3f} +/- {se[1]:.3f} per week | t0 = {p[2]:.2f} +/- {se[2]:.2f} weeks")
print(f"R^2 = {r2:.4f} | RMSE = {rmse:.1f} g")
target = 500
t_target = p[2] - np.log(p[0]/target - 1)/p[1]            # invert the logistic formula
print(f"Predicted week to reach {target} g: {t_target:.1f}")

pq, _ = curve_fit(quad, weeks, weight)
print(f"Quadratic fit RMSE: {np.sqrt(np.mean((weight - quad(weeks, *pq))**2)):.1f} g")
print(f"Prediction at week 40 -> logistic {logistic(40, *p):.0f} g | quadratic {quad(40, *pq):.0f} g (fish cannot shrink!)")

tt = np.linspace(0, 40, 300)
plt.scatter(weeks, weight, label="Measured"); plt.plot(tt, logistic(tt, *p), label="Logistic fit"); plt.plot(tt, quad(tt, *pq), "--", label="Quadratic fit")
plt.ylim(-100, 1300); plt.xlabel("Week"); plt.ylabel("Weight (g)"); plt.title("Tilapia growth curve"); plt.legend(); plt.grid(True)
plt.savefig(FIG / "task_14_modified.png", dpi=130, bbox_inches="tight"); plt.show()
