# Task 04: Floating-Point Arithmetic and Numerical Errors

**Course:** BIT 2118 Scientific Computing  |  **Student GitHub:** Just-Iann

## 1. The idea in my own words
Computers store numbers with a limited number of binary digits, so many decimals (like 0.1) cannot be stored exactly. Tiny errors are normal, but they can pile up, or get magnified when you subtract two nearly equal numbers. Absolute error is |true - approx|; relative error is that divided by |true|.

## 2. Handout program - inputs and operation
Program: [`code/Task_04_numerical_errors.py`](../code/Task_04_numerical_errors.py)

**Inputs:** 0.1 + 0.2 compared to 0.3; the approximation 1.414 for sqrt(2); and x = 1e-4, 1e-8, 1e-12 in the expression (sqrt(1+x) - 1)/x.

**Mathematical operation:** Exact equality vs `np.isclose`; absolute and relative error; and two algebraically identical formulas, the direct one and the rewritten stable one 1/(sqrt(1+x)+1).

<details><summary>Output of the handout program</summary>

```text
0.1 + 0.2 = 0.30000000000000004
Exact comparison: False
Tolerance-based comparison: True
approx=1.414: absolute=0.00021356, relative=0.01510114%
approx=1.41421: absolute=0.00000356, relative=0.00025190%

Unstable vs stable formula for (sqrt(1+x)-1)/x
x=1e-04: direct=0.499987500624, stable=0.499987500625
x=1e-08: direct=0.499999996961, stable=0.499999998750
x=1e-12: direct=0.500044450291, stable=0.500000000000
x=1e-16: direct=0.000000000000, stable=0.500000000000
```
</details>

## 3. I changed a parameter
**What I changed:** I used a better approximation of sqrt(2), 1.41421, and added an extra very small x = 1e-16.

**What happened:** With 1.41421 the absolute error dropped from 0.00021356 to 0.00000356 and the relative error from 0.0151% to 0.000252%, about 60 times better for two more correct digits. For x = 1e-16 the direct formula returned exactly 0 (because 1 + 1e-16 is stored as 1) while the true answer is 0.5, so it was 100% wrong. The stable formula still gave 0.5.

## 4. What the output means
`0.1 + 0.2` prints as 0.30000000000000004, so `==` says False but `np.isclose` says True: always compare floats with a tolerance. The direct formula slowly loses digits as x shrinks (0.50004445 at 1e-12 instead of 0.5) because of cancellation, which is a numerical error, not a mistake in the maths.


## 5. My own real-world case: Why money programs need care with decimals
Program: [`modified/Task_04_modified_money_precision.py`](../modified/Task_04_modified_money_precision.py)

**Assumptions:** One million deposits of KES 0.10 each, and daily revenues around KES 1 billion with a spread of about 10. All values are simulated.

**Input data:** Repeated 0.10 additions, the prices 1.10 and 2.20, and 1,000 random revenues near 1e9.

```text
Naive float sum     : 100000.00000133288  (error 1.333e-06)
math.fsum           : 100000.0
Decimal sum         : 100000.00

1.10 + 2.20 == 3.30 ? False | isclose: True | value: 3.3000000000000003

True variance ~ 100 | naive formula: 256.00 | stable formula: 97.27
```

**Interpretation:** Adding 0.10 a million times with plain floats gave 100000.00000133288, an error of about 1.3 millionths. `math.fsum` and `Decimal` both gave the exact 100000. `1.10 + 2.20 == 3.30` is False. The most dramatic case was the variance: the true spread is about 100, the careless formula E[x^2] - E[x]^2 returned 256 (more than double), while the two-pass formula gave 97.27. So for money I should use Decimal or whole cents, and for statistics on big numbers I should use stable formulas.
