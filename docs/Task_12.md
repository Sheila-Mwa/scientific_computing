# Task 12: Polynomial and Nonlinear Equation Solving

**Course:** BIT 2118 Scientific Computing  |  **Student GitHub:** Just-Iann

## 1. The idea in my own words
A nonlinear system has equations that are not straight lines, like circles and parabolas. A solver such as `scipy.optimize.root` starts from a guess and adjusts it until all the residuals (left side minus right side) are about zero. Different guesses can find different solutions, and sometimes there is no real solution.

## 2. Handout program - inputs and operation
Program: [`code/Task_12_nonlinear_equations.py`](../code/Task_12_nonlinear_equations.py)

**Inputs:** Circle x^2 + y^2 = 4 and parabola y = x^2 - 1, with starting guesses (1, 1) and (-1, 1).

**Mathematical operation:** Write each equation as a residual and let `root` find (x, y) that makes both residuals zero. Then print the residuals to verify.

<details><summary>Output of the handout program</summary>

```text
Radius 2.0  (handout)
  guess=[1.0, 1.0] -> [1.5175 1.3028]  residual=[-0. -0.]  converged=True
  guess=[-1.0, 1.0] -> [-1.5175  1.3028]  residual=[-0. -0.]  converged=True
Radius 1.5
  guess=[1.0, 1.0] -> [1.3133 0.7247]  residual=[0. 0.]  converged=True
  guess=[-1.0, 1.0] -> [-1.3133  0.7247]  residual=[0. 0.]  converged=True
Radius 0.5
  guess=[1.0, 1.0] -> [ 0.5005 -0.4997]  residual=[0.250206 0.249794]  converged=False
  guess=[-1.0, 1.0] -> [-0.5005 -0.4997]  residual=[0.250206 0.249794]  converged=False
```
</details>

## 3. I changed a parameter
**What I changed:** I changed the circle radius from 2 to 1.5 and to 0.5.

**What happened:** For radius 1.5 the intersections moved to (+/-1.3133, 0.7247). For radius 0.5 the solver reported `converged = False` and left residuals of about 0.25. That is correct: substituting x^2 = y + 1 gives y^2 + y + 1 - r^2 = 0, which needs r of at least 0.866 to have a real solution, so a tiny circle never touches the parabola.

## 4. What the output means
For the handout, the two curves meet at (1.5175, 1.3028) and (-1.5175, 1.3028). Residuals are zero, so both equations hold. The mirror-image points appear because the equations only contain x squared.


## 5. My own real-world case: Finding a phone's position from cell towers
Program: [`modified/Task_12_modified_cell_tower_position.py`](../modified/Task_12_modified_cell_tower_position.py)

**Assumptions:** A flat local map in km with towers at (0,0), (6,0) and (3,5). The phone is really at (2, 3). Measured distances have errors of about 15-20 m. This is a simplified trilateration, not how a real network does it.

**Input data:** Three measured distances 3.6206, 4.98 and 2.2501 km.

```text
Exact distances: [3.6056 5.     2.2361] | measured: [3.6206 4.98   2.2501]

Two towers give TWO candidate positions (two circle intersections):
  guess [2.0, 3.0] -> [2.026 3.001] | residual [-0. -0.] | distance to tower 3 = 2.224 (measured 2.250)
  guess [2.0, -3.0] -> [ 2.026 -3.001] | residual [-0. -0.] | distance to tower 3 = 8.060 (measured 2.250)
Third tower picks: [2.026 3.001]
Using all three towers (least squares): [2.019 2.989] | error vs true position: 22.1 m
With 300-400 m measurement errors: [2.492 2.799] | position error: 531 m
```

**Interpretation:** Two towers give two circle intersections, (2.026, 3.001) and (2.026, -3.001). The third tower resolves the ambiguity: the first candidate is 2.224 km from tower 3 (measured 2.250) while the other is 8.06 km away. Using all three towers with least squares gave (2.019, 2.989), an error of 22 m. When I increased the measurement errors to 300-400 m, the position error grew to about 531 m, so the accuracy of the answer is limited by the accuracy of the distances.
