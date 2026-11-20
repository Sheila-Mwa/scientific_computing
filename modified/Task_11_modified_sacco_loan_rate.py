"""Task 11 (modified): the true monthly interest rate of a SACCO loan.
Assumptions: borrow KES 1,200,000; repay KES 58,000 per month for 24 months (illustrative numbers).
Find r such that  58,000 * (1 - (1+r)^-24) / r  = 1,200,000."""
import numpy as np
from scipy.optimize import root_scalar

P, n, loan = 58_000.0, 24, 1_200_000.0
f  = lambda r: P * (1 - (1 + r)**-n) / r - loan
df = lambda r: P * (n*(1 + r)**(-n-1) / r - (1 - (1 + r)**-n) / r**2)

def newton_log(x0, steps=8):
    x, out = x0, [x0]
    for _ in range(steps):
        x = x - f(x)/df(x); out.append(x)
    return out

for r in newton_log(0.05, 6): print(f"  Newton iterate: r = {r:.10f}   f(r) = {f(r):+.3e}")
nw = root_scalar(f, fprime=df, x0=0.05, method="newton", xtol=1e-14)
sc = root_scalar(f, x0=0.01, x1=0.05, method="secant", xtol=1e-14)
bs = root_scalar(f, bracket=[1e-6, 0.2], method="bisect", xtol=1e-14)
print(f"\nNewton {nw.root:.8%} ({nw.iterations} it) | Secant {sc.root:.8%} ({sc.iterations} it) | Bisection {bs.root:.8%} ({bs.iterations} it)")
r = nw.root
print(f"Monthly rate {r:.4%} | nominal yearly {12*r:.2%} | effective yearly {(1+r)**12-1:.2%}")
print(f"Total repaid KES {P*n:,.0f} | total interest KES {P*n - loan:,.0f}")
print("\nWhat if the instalment is KES 62,000?")
P = 62_000.0
print(f"  monthly rate {root_scalar(f, x0=0.01, x1=0.05, method='secant').root:.4%}")
