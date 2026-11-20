# Task 19: Numerical Optimization

**Course:** BIT 2118 Scientific Computing  |  **Student GitHub:** Just-Iann

## 1. The idea in my own words
Optimisation finds the inputs that make an objective (like cost) as small as possible while respecting constraints (like a minimum capacity). `scipy.optimize.minimize` with SLSQP handles bounds and inequality constraints. If the answer must be whole numbers, the best continuous answer is only a starting point.

## 2. Handout program - inputs and operation
Program: [`code/Task_19_optimization.py`](../code/Task_19_optimization.py)

**Inputs:** Cost per unit: Type A = 12, Type B = 18. Capacity per unit: A = 100, B = 170. Need total capacity at least 1,000. Units cannot be negative.

**Mathematical operation:** Minimise 12x + 18y subject to 100x + 170y >= 1000 and x, y >= 0, then search whole-number combinations for comparison.

<details><summary>Output of the handout program</summary>

```text
cost_B=18.0: A=0.000, B=5.882, cost=105.88, success=True
   best whole-server combination (cost, A, B, capacity): (108.0, 0, 6, 1020.0)
cost_B=22.0: A=10.000, B=0.000, cost=120.00, success=True
   best whole-server combination (cost, A, B, capacity): (120.0, 10, 0, 1000.0)
cost_B=14.0: A=0.000, B=5.882, cost=82.35, success=True
   best whole-server combination (cost, A, B, capacity): (84.0, 0, 6, 1020.0)
```
</details>

## 3. I changed a parameter
**What I changed:** I changed the cost of a Type B unit from 18 to 22 and to 14.

**What happened:** At cost 18 the best plan is all Type B (5.882 units, cost 105.88). At cost 22 it flips to all Type A (10 units, cost 120). At cost 14 it stays all B (cost 82.35). The reason is cost per unit of capacity: A is 0.12, B is 0.106 at 18 and 0.129 at 22, and the cheaper source wins completely. The best whole-number plans cost 108, 120 and 84.

## 4. What the output means
The optimiser buys only the cheapest capacity and exactly meets the 1,000 requirement (capacity constraint active). With whole servers, 6 Type B gives 1,020 capacity for 108, slightly above the continuous cost 105.88.


## 5. My own real-world case: Cheapest mix of vans and buses for a SACCO route
Program: [`modified/Task_19_modified_matatu_fleet.py`](../modified/Task_19_modified_matatu_fleet.py)

**Assumptions:** Illustrative numbers: a 14-seater van costs KES 6,500/day and moves 14 x 8 = 112 passengers/day, a 33-seater bus costs KES 11,000/day and moves 33 x 6 = 198 passengers/day. We need at least 1,500 passengers/day, with parking for at most 12 vehicles. Whole vehicles are required.

**Input data:** Costs, capacities, requirement 1,500 (also tested 2,000), vehicle limit 12 (also tested 7).

```text
Cost per passenger: van 58.04, bus 55.56 KES
Need 1500/day, max 12 vehicles
  continuous optimum: vans 0.00, buses 7.58, cost KES 83,333, solver success True
  best whole-vehicle plan: cost KES 85,500 with 3 vans + 6 buses (capacity 1524)
  naive rounding-up gives (0, 8) -> KES 88,000
Need 2000/day, max 12 vehicles
  continuous optimum: vans 0.00, buses 10.10, cost KES 111,111, solver success True
  best whole-vehicle plan: cost KES 112,000 with 2 vans + 9 buses (capacity 2006)
  naive rounding-up gives (1, 11) -> KES 127,500
Need 1500/day, max 7 vehicles
  (solver reports no feasible continuous solution: Positive directional derivative for linesearch)
  continuous optimum: vans 0.00, buses 7.00, cost KES 77,000, solver success False
  no whole-vehicle plan satisfies the limits
  naive rounding-up gives (0, 8) -> KES 88,000
```

**Interpretation:** A bus costs KES 55.56 per passenger and a van 58.04, so the continuous optimum is 7.58 buses and no vans at KES 83,333. But we cannot buy 0.58 of a bus. Rounding up to 8 buses costs KES 88,000, while the best whole-vehicle plan is 6 buses + 3 vans at KES 85,500 (capacity 1,524), saving KES 2,500 per day. For 2,000 passengers the best plan is 9 buses + 2 vans at KES 112,000. With a limit of only 7 vehicles the demand of 1,500 cannot be met at all (7 buses give 1,386), and the solver and the search both report that no feasible plan exists. So rounding the continuous answer is not enough, and I have to check the integer combinations.
