# Task 07: Gaussian Elimination and LU Decomposition

**Course:** BIT 2118 Scientific Computing  |  **Student GitHub:** Just-Iann

## 1. The idea in my own words
Gaussian elimination turns a system into a triangle that is easy to solve from the bottom up. LU decomposition saves that elimination work as two triangular matrices (A = LU, with row swaps P for safety). If the same A appears again with a new b, I do not eliminate again, I just do two quick triangular solves.

## 2. Handout program - inputs and operation
Program: [`code/Task_07_gaussian_lu.py`](../code/Task_07_gaussian_lu.py)

**Inputs:** A 3x3 coefficient matrix that stays the same, and three different measurement vectors b.

**Mathematical operation:** `lu_factor(A)` once, then `lu_solve` for each b (forward and back substitution). Residual b - A x checks each answer, and `np.linalg.solve` is used as a comparison.

<details><summary>Output of the handout program</summary>

```text
Set 1: x=[5. 5. 5.]  residual norm=0.00e+00
Set 2: x=[5.31707317 5.26829268 4.75609756]  residual norm=1.78e-15
Set 3: x=[4.90243902 5.6097561  5.53658537]  residual norm=0.00e+00
Direct solve, set 1: [5. 5. 5.]

--- Parameter change: diagonal 4,4,3 -> 1.42 (almost singular) ---
Condition number A: 2.39 | condition number B: 489.8
A: solution shift for b+0.01: 0.0027915910103063868
B: solution shift for b+0.01: 0.8641056498951378
```
</details>

## 3. I changed a parameter
**What I changed:** I made the matrix almost singular by changing the diagonal from 4, 4, 3 to 1.42, then nudged the first entry of b by only 0.01 and measured how far the solution moved.

**What happened:** The condition number jumped from 2.39 to 489.8. The same 0.01 nudge moved the solution by 0.0028 for the original matrix but by 0.864 for the nearly singular one, roughly 300 times more. So the LU solver still worked, but the answer became very sensitive to tiny errors in the measurements.

## 4. What the output means
Set 1 gives x = [5, 5, 5], which I can check by hand: 4(5) - 5 = 15, -5 + 20 - 5 = 10, -5 + 15 = 10. The residual norms are about 1e-15 or 0, which is just round-off. The LU answers match `np.linalg.solve`.


## 5. My own real-world case: Hourly pressure drop in a small village water network
Program: [`modified/Task_07_modified_water_network.py`](../modified/Task_07_modified_water_network.py)

**Assumptions:** 4 junctions with fixed pipe conductances (matrix A never changes during the day). The right-hand side is a demand pattern with a morning peak and an evening peak. The solution x is a relative pressure drop below the reservoir level, in arbitrary units. For the speed test I used a 400-junction network with 500 demand vectors.

**Input data:** A = [[3,-1,0,0],[-1,3,-1,0],[0,-1,3,-1],[0,0,-1,2]], base demand [10, 6, 8, 4] scaled by the hourly pattern.

```text
Peak demand hour: 18 | pressure drop at junction 1 at peak: 6.35
Largest pressure drop overall: junction 3 value 7.62
Max residual over all 24 solves: 4.070144838902081e-15
500 solves of a 400x400 system: repeated solve 0.961s | LU once + reuse 0.036s | speed-up 27.1x
```

**Interpretation:** The biggest demand is at hour 18 (the evening peak) and at that hour the pressure drop at junction 1 is 6.35 units. Over the whole day the largest drop (7.62) is at junction 3. All 24 residuals are around 1e-15, so every solution is accurate. In the speed test, factoring once and reusing the factors was roughly 25 to 40 times faster than calling `solve` 500 times (0.96 s vs 0.036 s in my latest run; the ratio changes a bit between runs). That is why LU is worth it when the same network is solved every hour or every second with a new demand.
