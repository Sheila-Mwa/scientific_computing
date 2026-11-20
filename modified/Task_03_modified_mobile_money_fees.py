"""Task 3 (modified): tiered mobile-money fee on 1,000,000 transactions, loop vs vectorized.
Assumptions: HYPOTHETICAL fee tiers (not any real operator's tariff); 1 USD = 129 KES (assumed rate)."""
import numpy as np, timeit

KES_PER_USD = 129.0
EDGES = [100, 500, 1000, 5000]            # upper limits of the tiers (KES)
FEES = [0, 7, 13, 30, 60]                 # fee for each tier, last = above 5,000

rng = np.random.default_rng(2026)
amount = rng.lognormal(mean=np.log(450), sigma=1.0, size=1_000_000).round(0)

def fee_loop(values):
    out = []
    for a in values:
        if a <= 100: out.append(0)
        elif a <= 500: out.append(7)
        elif a <= 1000: out.append(13)
        elif a <= 5000: out.append(30)
        else: out.append(60)
    return out

def fee_vector(values):
    return np.select([values <= e for e in EDGES], FEES[:-1], default=FEES[-1])

t_loop = timeit.timeit(lambda: fee_loop(amount), number=1)
t_vec = timeit.timeit(lambda: fee_vector(amount), number=3) / 3
fees = fee_vector(amount)
print("Loop and vectorized results identical:", np.array_equal(fees, np.array(fee_loop(amount))))
print(f"Loop {t_loop:.3f}s | vectorized {t_vec:.4f}s | speed-up {t_loop/t_vec:.0f}x")
print(f"Median transaction: KES {np.median(amount):.0f} (USD {np.median(amount)/KES_PER_USD:.2f})")
print(f"Total value: KES {amount.sum():,.0f} | total fees: KES {fees.sum():,.0f} | average fee {fees.sum()/amount.sum():.2%} of value")
for lo, hi, name in ((0, 100, "<=100"), (100, 500, "101-500"), (500, 1000, "501-1000"), (1000, 5000, "1001-5000"), (5000, 1e12, ">5000")):
    share = ((amount > lo) & (amount <= hi)).mean()
    print(f"  tier {name:>9}: {share:.1%} of transactions")
