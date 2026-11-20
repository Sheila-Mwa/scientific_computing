"""Task 11 - Newton and secant for IRR. Parameter change = weaker last cash flow, bad starting guess."""
from scipy.optimize import root_scalar

def make(cash_flows):
    npv = lambda r: sum(cf/(1+r)**t for t, cf in enumerate(cash_flows))
    d_npv = lambda r: sum(-t*cf/(1+r)**(t+1) for t, cf in enumerate(cash_flows) if t > 0)
    return npv, d_npv

for label, cfs in (("Original", [-10000, 3000, 3500, 4000, 2500]),
                   ("Changed (last inflow 2500 -> 1500)", [-10000, 3000, 3500, 4000, 1500])):
    npv, d_npv = make(cfs)
    newton = root_scalar(npv, fprime=d_npv, x0=0.10, method="newton", xtol=1e-12)
    secant = root_scalar(npv, x0=0.05, x1=0.20, method="secant", xtol=1e-12)
    print(f"{label}\n  IRR Newton: {newton.root:.6%} ({newton.iterations} it)  Secant: {secant.root:.6%} ({secant.iterations} it)  NPV at root: {npv(newton.root):.2e}")

print("\nParameter change: different starting guesses x0 (original cash flows)")
npv, d_npv = make([-10000, 3000, 3500, 4000, 2500])
for x0 in (0.01, 0.10, 0.50, 1.00):
    r = root_scalar(npv, fprime=d_npv, x0=x0, method="newton", xtol=1e-12)
    print(f"  x0={x0:<5}: IRR = {r.root:.6%} after {r.iterations} iterations")
