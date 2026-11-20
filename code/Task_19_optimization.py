"""Task 19 - Constrained optimisation. Parameter change = cost of a Type B unit."""
import numpy as np
from scipy.optimize import minimize

def solve(cost_b, cost_a=12.0, cap_a=100.0, cap_b=170.0, required=1000.0):
    res = minimize(lambda z: cost_a*z[0] + cost_b*z[1], x0=[5, 3], method="SLSQP",
                   bounds=[(0, None), (0, None)],
                   constraints={"type": "ineq", "fun": lambda z: cap_a*z[0] + cap_b*z[1] - required})
    best = None
    for a in range(20):
        for b in range(20):
            if cap_a*a + cap_b*b >= required:
                c = cost_a*a + cost_b*b
                if best is None or c < best[0]: best = (c, a, b, cap_a*a + cap_b*b)
    print(f"cost_B={cost_b}: A={res.x[0]:.3f}, B={res.x[1]:.3f}, cost={res.fun:.2f}, success={res.success}")
    print(f"   best whole-server combination (cost, A, B, capacity): {best}")

solve(18.0)   # handout
solve(22.0)   # change
solve(14.0)   # change
