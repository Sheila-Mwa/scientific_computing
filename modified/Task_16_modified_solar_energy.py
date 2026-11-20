"""Task 16 (modified): daily energy from a rooftop solar array, 06:00-18:00.
Assumptions: ideal clear-day power P(t) = 4.2 sin(pi (t-6)/12) kW; a cloudy day multiplies some hours by a factor.
Electricity valued at an assumed KES 28 per kWh."""
import numpy as np
from scipy.integrate import simpson, quad

trap = getattr(np, "trapezoid", None) or np.trapz
t = np.arange(6, 19, dtype=float)                                   # hourly readings
clear = 4.2*np.sin(np.pi*(t - 6)/12)
exact, _ = quad(lambda x: 4.2*np.sin(np.pi*(x - 6)/12), 6, 18)
print(f"Clear day exact: {exact:.4f} kWh (= 4.2*24/pi = {4.2*24/np.pi:.4f})")
print(f"  trapezoid {trap(clear, t):.4f} (error {abs(trap(clear, t)-exact):.4f}) | Simpson {simpson(clear, x=t):.4f} (error {abs(simpson(clear, x=t)-exact):.5f})")

sub = slice(0, None, 3)                                              # only every 3rd hour
print(f"  only 5 readings (every 3 h): trapezoid {trap(clear[sub], t[sub]):.3f} | Simpson {simpson(clear[sub], x=t[sub]):.3f}")

cloud = np.ones_like(t); cloud[[5, 6, 8, 9]] = [0.35, 0.3, 0.45, 0.6]   # clouds around 11:00-12:00 and 14:00-15:00
cloudy = clear*cloud
e_cloudy = simpson(cloudy, x=t)
print(f"\nCloudy day (measured hourly): {e_cloudy:.3f} kWh ({e_cloudy/exact:.0%} of a clear day)")
print(f"Value of clear day: KES {exact*28:,.0f} | cloudy day: KES {e_cloudy*28:,.0f} | loss KES {(exact-e_cloudy)*28:,.0f}")
