# BIT 2118 Scientific Computing - Group Work 

### Name: Sheila Njeri Mwangi
### Registration Number: BSCCS/2025/68619
### Course: Bsc. Computer Science

This repository is my own submission for the Scientific Computing group work. We discussed the tasks as a group, but the code, data and write-ups here are my own. For every task I did what the instructions ask:

1. **Identify the inputs and the mathematical operation** (section 2 of each write-up).
2. **Change at least one parameter** and explain how the result changes (section 3).
3. **Explain the output in words** and interpret graphs where there are any (section 4).
4. **Modify the program for a different, related real-world case**, with the assumptions, input data, output and interpretation written down (section 5).

For the new cases I tried to use situations from daily life in Kenya (matatus, water tanks, mobile money, SACCO loans, solar, farming) instead of repeating the handout examples.

## Contents

Task numbers follow the handout (the letters A-S are the section letters used in the PDF).

| Task | Topic | Documentation | Handout program + parameter change | My new case |
|---|---|---|---|---|
| 02 (A) | NumPy Arrays and Numerical Computation | [write-up](docs/Task_02.md) | [`Task_02_numpy_arrays.py`](code/Task_02_numpy_arrays.py) | [`Task_02_modified_water_tank.py`](modified/Task_02_modified_water_tank.py) - Water level in a rooftop tank (rationed supply) |
| 03 (B) | Mathematical Functions and Vectorization | [write-up](docs/Task_03.md) | [`Task_03_vectorization.py`](code/Task_03_vectorization.py) | [`Task_03_modified_mobile_money_fees.py`](modified/Task_03_modified_mobile_money_fees.py) - Tiered mobile-money fees on a million transactions |
| 04 (C) | Floating-Point Arithmetic and Numerical Errors | [write-up](docs/Task_04.md) | [`Task_04_numerical_errors.py`](code/Task_04_numerical_errors.py) | [`Task_04_modified_money_precision.py`](modified/Task_04_modified_money_precision.py) - Why money programs need care with decimals |
| 05 (D) | Matrix Algebra and Matrix Operations | [write-up](docs/Task_05.md) | [`Task_05_matrix_algebra.py`](code/Task_05_matrix_algebra.py) | [`Task_05_modified_land_plot.py`](modified/Task_05_modified_land_plot.py) - Re-drawing a farm plot on a rotated, stretched map |
| 06 (E) | Solution of Systems of Linear Equations | [write-up](docs/Task_06.md) | [`Task_06_linear_systems.py`](code/Task_06_linear_systems.py) | [`Task_06_modified_feed_mix.py`](modified/Task_06_modified_feed_mix.py) - Blending 100 kg of dairy feed from three ingredients |
| 07 (F) | Gaussian Elimination and LU Decomposition | [write-up](docs/Task_07.md) | [`Task_07_gaussian_lu.py`](code/Task_07_gaussian_lu.py) | [`Task_07_modified_water_network.py`](modified/Task_07_modified_water_network.py) - Hourly pressure drop in a small village water network |
| 08 (G) | Iterative Methods for Linear Systems | [write-up](docs/Task_08.md) | [`Task_08_iterative_linear.py`](code/Task_08_iterative_linear.py) | [`Task_08_modified_solar_dryer.py`](modified/Task_08_modified_solar_dryer.py) - Temperature on a solar drying tray (2-D grid) |
| 09 (H) | Eigenvalues and Eigenvectors | [write-up](docs/Task_09.md) | [`Task_09_eigenvalues.py`](code/Task_09_eigenvalues.py) | [`Task_09_modified_matatu_network.py`](modified/Task_09_modified_matatu_network.py) - Which matatu stage matters most? |
| 10 (I) | Root Finding: Bisection and Fixed-Point Methods | [write-up](docs/Task_10.md) | [`Task_10_bisection_fixed_point.py`](code/Task_10_bisection_fixed_point.py) | [`Task_10_modified_horizontal_tank.py`](modified/Task_10_modified_horizontal_tank.py) - Water depth in a horizontal cylindrical tank |
| 11 (J) | Root Finding: Newton-Raphson and Secant Methods | [write-up](docs/Task_11.md) | [`Task_11_newton_secant.py`](code/Task_11_newton_secant.py) | [`Task_11_modified_sacco_loan_rate.py`](modified/Task_11_modified_sacco_loan_rate.py) - The true interest rate of a SACCO loan |
| 12 (K) | Polynomial and Nonlinear Equation Solving | [write-up](docs/Task_12.md) | [`Task_12_nonlinear_equations.py`](code/Task_12_nonlinear_equations.py) | [`Task_12_modified_cell_tower_position.py`](modified/Task_12_modified_cell_tower_position.py) - Finding a phone's position from cell towers |
| 13 (L) | Interpolation | [write-up](docs/Task_13.md) | [`Task_13_interpolation.py`](code/Task_13_interpolation.py) | [`Task_13_modified_thika_road_speed.py`](modified/Task_13_modified_thika_road_speed.py) - Filling in traffic speed between hourly readings |
| 14 (M) | Curve Fitting and Approximation | [write-up](docs/Task_14.md) | [`Task_14_curve_fitting.py`](code/Task_14_curve_fitting.py) | [`Task_14_modified_tilapia_growth.py`](modified/Task_14_modified_tilapia_growth.py) - Growth curve of farmed tilapia |
| 15 (N) | Numerical Differentiation | [write-up](docs/Task_15.md) | [`Task_15_numerical_differentiation.py`](code/Task_15_numerical_differentiation.py) | [`Task_15_modified_tank_outflow.py`](modified/Task_15_modified_tank_outflow.py) - How fast is a water tank emptying? |
| 16 (O) | Numerical Integration | [write-up](docs/Task_16.md) | [`Task_16_numerical_integration.py`](code/Task_16_numerical_integration.py) | [`Task_16_modified_solar_energy.py`](modified/Task_16_modified_solar_energy.py) - Daily energy from a rooftop solar array |
| 17 (P) | Ordinary Differential Equations - Euler Method | [write-up](docs/Task_17.md) | [`Task_17_euler_ode.py`](code/Task_17_euler_ode.py) | [`Task_17_modified_tank_draining.py`](modified/Task_17_modified_tank_draining.py) - A water tank draining through a hole |
| 18 (Q) | Numerical Solution of ODEs Using SciPy | [write-up](docs/Task_18.md) | [`Task_18_scipy_ode.py`](code/Task_18_scipy_ode.py) | [`Task_18_modified_matatu_suspension.py`](modified/Task_18_modified_matatu_suspension.py) - A matatu body bouncing after a speed bump |
| 19 (R) | Numerical Optimization | [write-up](docs/Task_19.md) | [`Task_19_optimization.py`](code/Task_19_optimization.py) | [`Task_19_modified_matatu_fleet.py`](modified/Task_19_modified_matatu_fleet.py) - Cheapest mix of vans and buses for a SACCO route |
| 20 (S) | Random Numbers and Monte Carlo Methods | [write-up](docs/Task_20.md) | [`Task_20_monte_carlo.py`](code/Task_20_monte_carlo.py) | [`Task_20_modified_trip_time_risk.py`](modified/Task_20_modified_trip_time_risk.py) - Will I get to an 08:00 class on time? |

## Folder layout

```
code/        handout programs (with my parameter-change experiment added at the end)
modified/    my new real-world versions of each program
docs/        one write-up per task (inputs, change, interpretation, new case)
figures/     graphs saved by the programs
outputs/     the text printed by each program when I ran it
run_all.sh   runs everything again
```

## How to run

```bash
pip install -r requirements.txt
bash run_all.sh                 # everything
cd code && python Task_08_iterative_linear.py   # or a single program
```

NumPy 2.x is needed because the integration task uses `np.trapezoid` (the code falls back to `np.trapz` in my modified version). Graphs are saved in `figures/` and shown on screen if your setup has a display.

## Honest notes about the data

- All numbers in my new cases are **made up for practice** (illustrative values and simulated data), for example the mobile-money fee tiers, the tank readings, the traffic speeds and the SACCO loan. They are not real measurements and not real tariffs, and the conclusions only apply to these assumptions.
- Random simulations use fixed seeds so the results are repeatable. Timing results (the loop-vs-vectorized speed-ups) change a little from computer to computer.

## A few things I took away

- One bad data point can wreck a least-squares fit (Task 14) and a mean (Task 2), so looking at residuals and more than one statistic matters.
- A method can be mathematically correct and still fail: fixed-point iteration diverged when the slope was above 1 (Task 10), and Euler blew up when the step was too large (Task 17).
- A solver can return an answer that is not physically allowed, such as negative fish meal in a feed recipe (Task 6) or half a bus (Task 19), so I must check the answer against the real situation.
- Accuracy depends on how the data was collected as much as on the method, for example the integration with too few readings (Task 16) and the position error from cell tower distances (Task 12).
