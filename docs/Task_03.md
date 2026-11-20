# Task 03: Mathematical Functions and Vectorization

**Course:** BIT 2118 Scientific Computing  |  **Student GitHub:** Just-Iann

## 1. The idea in my own words
Vectorization means giving NumPy a whole array and letting it apply the operation in fast compiled code, instead of Python visiting each number one at a time. The result is the same, only much quicker, and the code is shorter.

## 2. Handout program - inputs and operation
Program: [`code/Task_03_vectorization.py`](../code/Task_03_vectorization.py)

**Inputs:** 1,000,000 random network latencies between 5 and 250 ms (random seed 42 so the data is repeatable).

**Mathematical operation:** Convert each value from milliseconds to seconds (divide by 1000) and square it. Done once with a Python `for` loop and once with `(x/1000)**2` on the whole array, and timed with `timeit`.

<details><summary>Output of the handout program</summary>

```text
N=1,000,000  loop=0.1829s  vectorized=0.01724s  speed-up=11x
   first five squared values: [0.03787665 0.01266192 0.04637842 0.03092504 0.00078812]
N=  100,000  loop=0.0165s  vectorized=0.00013s  speed-up=124x
N=3,000,000  loop=0.9672s  vectorized=0.03917s  speed-up=25x
```
</details>

## 3. I changed a parameter
**What I changed:** I changed the number of readings N from 1,000,000 to 100,000 and to 3,000,000.

**What happened:** The loop time grows roughly in proportion to N (0.017 s, 0.18 s, 0.97 s for 100k, 1M, 3M in my latest run) while the vectorized version stays at hundredths of a second or less. The speed-up was 124x, 11x and 25x. That number is not stable from run to run because it depends on the machine, memory allocation and warm-up (an earlier run of mine gave 112x, 21x and 73x). The reliable conclusion is that vectorized code was roughly 10 to 120 times faster here, and the absolute time saved grows with N.

## 4. What the output means
The first five squared values (about 0.038, 0.013, 0.046, ...) are in seconds squared and would be used to compute an error measure. The important output is the timing comparison: same answers, far less waiting.


## 5. My own real-world case: Tiered mobile-money fees on a million transactions
Program: [`modified/Task_03_modified_mobile_money_fees.py`](../modified/Task_03_modified_mobile_money_fees.py)

**Assumptions:** The fee tiers are hypothetical (0 up to 100 KES, 7 up to 500, 13 up to 1,000, 30 up to 5,000, 60 above) and are not any real operator's tariff. Exchange rate assumed 1 USD = 129 KES. Transaction sizes are randomly generated (lognormal, median 450 KES).

**Input data:** 1,000,000 simulated transaction amounts in KES.

```text
Loop and vectorized results identical: True
Loop 0.136s | vectorized 0.0155s | speed-up 9x
Median transaction: KES 450 (USD 3.49)
Total value: KES 742,450,201 | total fees: KES 13,120,227 | average fee 1.77% of value
  tier     <=100: 6.7% of transactions
  tier   101-500: 47.6% of transactions
  tier  501-1000: 24.5% of transactions
  tier 1001-5000: 20.4% of transactions
  tier     >5000: 0.8% of transactions
```

**Interpretation:** `np.select` applied a different fee per tier to every transaction at once and gave exactly the same answer as the loop (`True`), about 9 times faster here. The median transaction was KES 450 (about USD 3.49). Total value was about KES 742 million and the fees about KES 13.1 million, an average of 1.77% of value. Nearly half of all transactions (47.6%) fall in the 101-500 KES tier, so small payments carry most of the fee count. In a tiered system like this, a small payment such as 101 KES paying 7 KES is charged about 7% while a 5,000+ payment paying 60 KES is charged around 1% or less, so the fee is heavy on small senders.
