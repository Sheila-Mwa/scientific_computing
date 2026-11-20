"""Task 12 - Circle/parabola intersection. Parameter change = radius."""
import numpy as np
from scipy.optimize import root

def run(radius, guesses):
    eqs = lambda z: [z[0]**2 + z[1]**2 - radius**2, z[1] - (z[0]**2 - 1)]
    for guess in guesses:
        s = root(eqs, guess)
        print(f"  guess={guess} -> {np.round(s.x, 4)}  residual={np.round(eqs(s.x), 6)}  converged={s.success}")

for r in (2.0, 1.5, 0.5):
    print(f"Radius {r}" + ("  (handout)" if r == 2.0 else ""))
    run(r, ([1.0, 1.0], [-1.0, 1.0]))
