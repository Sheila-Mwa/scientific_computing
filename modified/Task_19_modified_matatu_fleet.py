"""Task 19 (modified): cheapest mix of 14-seater vans and 33-seater buses for a SACCO route.
Assumptions (illustrative): van costs KES 6,500/day and moves 14 x 8 = 112 passengers/day; bus costs KES 11,000/day
and moves 33 x 6 = 198 passengers/day. Need >= 1,500 passengers/day. Parking limit: at most 12 vehicles."""
import numpy as np
from scipy.optimize import minimize

cost_van, cost_bus, cap_van, cap_bus = 6500., 11000., 112., 198.

def solve(required=1500., max_vehicles=12):
    res = minimize(lambda z: (cost_van*z[0] + cost_bus*z[1]) / 1000, x0=[1, 6], method="SLSQP", bounds=[(0, None), (0, None)],
                   constraints=[{"type": "ineq", "fun": lambda z: cap_van*z[0] + cap_bus*z[1] - required},
                                {"type": "ineq", "fun": lambda z: max_vehicles - z[0] - z[1]}])
    best = None
    for v in range(0, max_vehicles + 1):
        for b in range(0, max_vehicles + 1 - v):
            if cap_van*v + cap_bus*b >= required:
                c = cost_van*v + cost_bus*b
                if best is None or c < best[0]: best = (c, v, b, cap_van*v + cap_bus*b)
    print(f"Need {required:.0f}/day, max {max_vehicles} vehicles")
    if not res.success: print("  (solver reports no feasible continuous solution:", res.message + ")")
    print(f"  continuous optimum: vans {res.x[0]:.2f}, buses {res.x[1]:.2f}, cost KES {res.fun*1000:,.0f}, solver success {res.success}")
    if best: print(f"  best whole-vehicle plan: cost KES {best[0]:,.0f} with {best[1]} vans + {best[2]} buses (capacity {best[3]:.0f})")
    else: print("  no whole-vehicle plan satisfies the limits")
    naive = int(np.ceil(res.x[0])), int(np.ceil(res.x[1]))
    print(f"  naive rounding-up gives {naive} -> KES {cost_van*naive[0] + cost_bus*naive[1]:,.0f}")

print(f"Cost per passenger: van {cost_van/cap_van:.2f}, bus {cost_bus/cap_bus:.2f} KES")
solve()
solve(required=2000.0)
solve(required=1500.0, max_vehicles=7)
