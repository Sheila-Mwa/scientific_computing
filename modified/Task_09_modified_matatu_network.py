"""Task 9 (modified): which matatu stage is structurally most important?
Assumptions: SIMPLIFIED, hypothetical links between 7 Nairobi stages; an edge means a direct route."""
import numpy as np

nodes = ["CBD", "Westlands", "Kasarani", "Rongai", "Embakasi", "Kikuyu", "Eastleigh"]
edges = [("CBD", "Westlands"), ("CBD", "Kasarani"), ("CBD", "Rongai"), ("CBD", "Embakasi"),
         ("CBD", "Kikuyu"), ("CBD", "Eastleigh"), ("Westlands", "Kikuyu"),
         ("Kasarani", "Eastleigh"), ("Embakasi", "Eastleigh")]

def adjacency(nodes, edges):
    A = np.zeros((len(nodes), len(nodes)))
    for u, v in edges:
        A[nodes.index(u), nodes.index(v)] = A[nodes.index(v), nodes.index(u)] = 1
    return A

def centrality(A):
    vals, vecs = np.linalg.eigh(A)                    # symmetric matrix -> eigh
    v = np.abs(vecs[:, -1]); return vals[-1], v / v.sum()

def power_iteration(A, steps=200):
    v = np.ones(len(A))
    for _ in range(steps):
        v = A @ v; v /= np.linalg.norm(v)
    return v @ A @ v, v / v.sum()

A = adjacency(nodes, edges)
lam, c = centrality(A)
print("Largest eigenvalue:", round(lam, 4))
for n, s in sorted(zip(nodes, c), key=lambda t: -t[1]): print(f"  {n:10s} {s:.4f}  (links: {int(A[nodes.index(n)].sum())})")
lam_p, c_p = power_iteration(A)
print("Power-iteration check agrees:", np.allclose(c, c_p, atol=1e-6))

# What if the CBD stage is closed (e.g. matatus banned from the CBD)?
from scipy.sparse.csgraph import connected_components
keep = [i for i, n in enumerate(nodes) if n != "CBD"]
A2 = A[np.ix_(keep, keep)]
n_comp, labels = connected_components(A2)
print("\nCBD closed: largest eigenvalue", round(np.linalg.eigvalsh(A2)[-1], 4), "| separate groups of stages:", n_comp)
for k in range(n_comp):
    print("  group", k + 1, ":", [nodes[keep[i]] for i in np.flatnonzero(labels == k)])
