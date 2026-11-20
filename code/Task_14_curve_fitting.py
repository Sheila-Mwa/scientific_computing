"""Task 14 - Curve fitting. Parameter change = one bad measurement (outlier) at 250 users."""
import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt
from pathlib import Path
FIG = Path(__file__).resolve().parent.parent / "figures"

users = np.array([50, 100, 150, 200, 250, 300, 350], dtype=float)
model = lambda x, a, b, c: a*x**2 + b*x + c

def fit(y, label):
    p, _ = curve_fit(model, users, y)
    rmse = np.sqrt(np.mean((y - model(users, *p))**2))
    print(f"{label}: y = {p[0]:.6f}x^2 + {p[1]:.4f}x + {p[2]:.2f} | RMSE {rmse:.2f} ms | prediction at 400 users {model(400, *p):.1f} ms")
    return p

y = np.array([82, 95, 115, 145, 185, 238, 305], dtype=float)
p = fit(y, "Original      ")
y_bad = y.copy(); y_bad[4] = 300.0      # outlier
p_bad = fit(y_bad, "With outlier  ")

xp = np.linspace(50, 400, 300)
plt.scatter(users, y, label="Measurements"); plt.plot(xp, model(xp, *p), label="Fitted curve")
plt.xlabel("Concurrent users"); plt.ylabel("Response time (ms)"); plt.title("Server response-time curve fitting")
plt.legend(); plt.grid(True); plt.savefig(FIG / "task_14_original.png", dpi=130, bbox_inches="tight"); plt.show()
