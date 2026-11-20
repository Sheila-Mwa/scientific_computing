"""Task 4 (modified): why money software must be careful with floats.
Assumptions: 1,000,000 deposits of KES 0.10; daily revenues near KES 1 billion."""
import numpy as np, math
from decimal import Decimal

# 1. Adding 0.10 a million times
naive = 0.0
for _ in range(1_000_000):
    naive += 0.10
exact = Decimal("0.10") * 1_000_000
print(f"Naive float sum     : {naive!r}  (error {abs(naive - 100000):.3e})")
print(f"math.fsum           : {math.fsum([0.10]*1_000_000)!r}")
print(f"Decimal sum         : {exact}")

# 2. Prices in shillings and cents
print("\n1.10 + 2.20 == 3.30 ?", 1.10 + 2.20 == 3.30, "| isclose:", np.isclose(1.10 + 2.20, 3.30), "| value:", 1.10 + 2.20)

# 3. Variance of big numbers with tiny spread: catastrophic cancellation
rng = np.random.default_rng(1)
revenue = 1e9 + rng.normal(0, 10, 1000)                  # true std about 10
naive_var = np.mean(revenue**2) - np.mean(revenue)**2    # textbook shortcut formula
stable_var = np.mean((revenue - revenue.mean())**2)      # two-pass formula
print(f"\nTrue variance ~ 100 | naive formula: {naive_var:.2f} | stable formula: {stable_var:.2f}")
