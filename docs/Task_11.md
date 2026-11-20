# Task 11: Root Finding: Newton-Raphson and Secant Methods

**Course:** BIT 2118 Scientific Computing  |  **Student GitHub:** Just-Iann

## 1. The idea in my own words
Newton-Raphson follows the tangent line down to the x-axis again and again: x_new = x - f(x)/f'(x). It is very fast near a root. The secant method does the same without needing a derivative, using the line through the last two points. Both need a reasonable starting guess.

## 2. Handout program - inputs and operation
Program: [`code/Task_11_newton_secant.py`](../code/Task_11_newton_secant.py)

**Inputs:** Cash flows -10,000, 3,000, 3,500, 4,000, 2,500 over years 0 to 4, with starting guess 0.10 for Newton and 0.05 and 0.20 for secant.

**Mathematical operation:** Find the rate r where the net present value NPV(r) = sum of cash_t/(1+r)^t equals zero. This r is the internal rate of return (IRR).

<details><summary>Output of the handout program</summary>

```text
Original
  IRR Newton: 11.542461% (4 it)  Secant: 11.542461% (7 it)  NPV at root: 2.27e-12
Changed (last inflow 2500 -> 1500)
  IRR Newton: 8.269087% (4 it)  Secant: 8.269087% (6 it)  NPV at root: 3.87e-12

Parameter change: different starting guesses x0 (original cash flows)
  x0=0.01 : IRR = 11.542461% after 5 iterations
  x0=0.1  : IRR = 11.542461% after 4 iterations
  x0=0.5  : IRR = 11.542461% after 8 iterations
  x0=1.0  : IRR = -154.411050% after 7 iterations
```
</details>

## 3. I changed a parameter
**What I changed:** First I reduced the last inflow from 2,500 to 1,500. Second I tried different Newton starting guesses (0.01, 0.10, 0.50 and 1.00).

**What happened:** Smaller final inflow lowered the IRR from 11.54% to 8.27%, as expected, because the project earns less. The starting guess mattered: 0.01, 0.10 and 0.50 all found 11.54% (in 5, 4 and 8 iterations), but a start at 1.0 converged to -154.4%, a different mathematical root that has no financial meaning. So Newton is fast but I must start near a sensible value.

## 4. What the output means
IRR = 11.542461% from both methods, and NPV at that rate is about 1e-12, i.e. zero. It means the investment behaves like putting money in an account paying 11.54% a year.


## 5. My own real-world case: The true interest rate of a SACCO loan
Program: [`modified/Task_11_modified_sacco_loan_rate.py`](../modified/Task_11_modified_sacco_loan_rate.py)

**Assumptions:** A loan of KES 1,200,000 repaid with 24 monthly instalments of KES 58,000. The numbers are illustrative. I solved 58,000 (1 - (1+r)^-24)/r = 1,200,000 for the monthly rate r, with my own derivative, and compared Newton, secant and bisection.

**Input data:** P = 58,000, n = 24, loan = 1,200,000, start guess 0.05 for Newton, 0.01 and 0.05 for secant.

```text
Newton iterate: r = 0.0500000000   f(r) = -3.997e+05
  Newton iterate: r = -0.0013383107   f(r) = +2.156e+05
  Newton iterate: r = 0.0107655264   f(r) = +2.096e+04
  Newton iterate: r = 0.0122129915   f(r) = +2.523e+02
  Newton iterate: r = 0.0122308422   f(r) = +3.764e-02
  Newton iterate: r = 0.0122308449   f(r) = +6.752e-09
  Newton iterate: r = 0.0122308449   f(r) = -2.561e-09

Newton 1.22308449% (6 it) | Secant 1.22308449% (7 it) | Bisection 1.22308449% (45 it)
Monthly rate 1.2231% | nominal yearly 14.68% | effective yearly 15.71%
Total repaid KES 1,392,000 | total interest KES 192,000

What if the instalment is KES 62,000?
  monthly rate 1.7976%
```

**Interpretation:** The monthly rate is 1.2231% (14.68% nominal per year, 15.71% effective per year). Total repaid is KES 1,392,000, so the interest is KES 192,000. Newton converged in 6 iterations, secant in 7 and bisection needed 45. With a start of 0.05, the first Newton step overshot to a negative rate (-0.13%) before coming back, which shows why a good starting guess helps. If the instalment were KES 62,000 instead the rate would be 1.80% per month, so a borrower can see how much a bigger instalment costs when the loan size is the same.
