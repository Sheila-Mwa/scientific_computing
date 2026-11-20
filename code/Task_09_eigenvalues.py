"""Task 9 - Eigenvector centrality. Parameter change = add / remove network links."""
import numpy as np

nodes = ["A", "B", "C", "D"]
def centrality(adj):
    vals, vecs = np.linalg.eig(adj)
    i = np.argmax(np.real(vals))
    v = np.abs(np.real(vecs[:, i]))
    return np.real(vals[i]), v / v.sum(), np.real(vecs[:, i])

A = np.array([[0,1,1,0],[1,0,1,1],[1,1,0,1],[0,1,1,0]], dtype=float)
lam, c, v = centrality(A)
print("Original  dominant eigenvalue:", round(lam, 4))
for n, s in zip(nodes, c): print(f"  {n}: {s:.4f}")
print("  Verification error:", np.linalg.norm(A @ v - lam * v))

A2 = A.copy(); A2[0, 3] = A2[3, 0] = 1          # change 1: link A-D
lam2, c2, _ = centrality(A2)
print("\nAfter adding link A-D  eigenvalue:", round(lam2, 4), "scores:", np.round(c2, 4))
A3 = A.copy(); A3[1, 2] = A3[2, 1] = 0          # change 2: remove link B-C
lam3, c3, _ = centrality(A3)
print("After removing link B-C eigenvalue:", round(lam3, 4), "scores:", np.round(c3, 4))
