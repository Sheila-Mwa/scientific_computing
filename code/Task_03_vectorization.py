"""Task 3 - Vectorization: loop vs NumPy. Parameter change = number of readings N."""
import numpy as np
import timeit

def make_latency(n, seed=42):
    return np.random.default_rng(seed).uniform(5, 250, n)   # ms

def loop_version(latency_ms):
    squared = []
    for value in latency_ms:
        seconds = value / 1000.0
        squared.append(seconds ** 2)
    return squared

def vectorized_version(latency_ms):
    seconds = latency_ms / 1000.0
    return seconds ** 2

# Part 1 = handout (N = 1,000,000), Part 2 = other values of N
for n in (1_000_000, 100_000, 3_000_000):
    data = make_latency(n)
    loop_time = timeit.timeit(lambda: loop_version(data), number=1)
    vec_time = timeit.timeit(lambda: vectorized_version(data), number=3) / 3
    print(f"N={n:>9,}  loop={loop_time:.4f}s  vectorized={vec_time:.5f}s  speed-up={loop_time/vec_time:.0f}x")
    if n == 1_000_000:
        print("   first five squared values:", vectorized_version(data)[:5])
