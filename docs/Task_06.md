# Task 06: Solution of Systems of Linear Equations

**Course:** BIT 2118 Scientific Computing  |  **Student GitHub:** Just-Iann

## 1. The idea in my own words
When several unknowns must satisfy several equations at once, I write them as Ax = b and solve for x. Each row of A is one equation. If A is invertible there is exactly one answer, and I can always check it by computing A x and comparing with b.

## 2. Handout program - inputs and operation
Program: [`code/Task_06_linear_systems.py`](../code/Task_06_linear_systems.py)

**Inputs:** A = [[4, 2], [8, 12]] (CPU and memory use per server type) and b = [20, 72] (total CPU and memory).

**Mathematical operation:** `np.linalg.solve(A, b)` (an LU-based solver), then the residual b - A x and its norm to verify.

<details><summary>Output of the handout program</summary>

```text
Original totals (20 CPU, 72 GB)
  Type A, Type B servers: [3. 4.]
  A @ x: [20. 72.] | residual norm: 0.0
Changed totals  (22 CPU, 72 GB)
  Type A, Type B servers: [3.75 3.5 ]
  A @ x: [22. 72.] | residual norm: 0.0
Condition number of A: 6.982
```
</details>

## 3. I changed a parameter
**What I changed:** I changed the observed CPU total from 20 to 22 (memory stays 72).

**What happened:** The answer changed from (3, 4) to (3.75, 3.5). Fractions of a server cannot exist, so the new totals cannot be produced by whole servers. In practice it would mean a measurement error or another server type. The condition number of A is about 7, so the system is well behaved: small changes in b give proportionally small changes in x.

## 4. What the output means
3 Type A and 4 Type B servers: 4(3) + 2(4) = 20 CPU and 8(3) + 12(4) = 72 GB, which matches. The residual is 0, so the solution is verified.


## 5. My own real-world case: Blending 100 kg of dairy feed from three ingredients
Program: [`modified/Task_06_modified_feed_mix.py`](../modified/Task_06_modified_feed_mix.py)

**Assumptions:** Maize germ, sunflower cake and fish meal (omena). The protein and energy values per kg are illustrative, not lab values. The three equations are total mass = 100 kg, protein = 21.9 kg, energy = 1,200 MJ.

**Input data:** A = [[1,1,1],[0.09,0.35,0.60],[13,10,12]], b = [100, 21.9, 1200].

```text
kg of maize germ, sunflower cake, fish meal: [60. 30. 10.]
All amounts non-negative: True
Check A @ x: [ 100.    21.9 1200. ] | residual norm: 0.0
Condition number: 130.44 | determinant: 1.27

Protein target 10 kg -> [ 78.74  39.37 -18.11] | all non-negative: False
```

**Interpretation:** The solution is 60 kg maize germ, 30 kg sunflower cake and 10 kg fish meal, all positive and with residual 0. The condition number is about 130, much higher than the server example, so the recipe is sensitive to errors in the nutrient figures. When I changed the protein target to only 10 kg the maths still returned an answer, but fish meal came out at -18 kg, which is impossible. That showed me that a linear solver can return a valid solution that is not physically allowed, so the sign of every unknown must be checked.
