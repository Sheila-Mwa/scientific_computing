# Task 09: Eigenvalues and Eigenvectors

**Course:** BIT 2118 Scientific Computing  |  **Student GitHub:** Just-Iann

## 1. The idea in my own words
An eigenvector of a matrix is a direction that the matrix only stretches, never turns: A v = lambda v. For a network's adjacency matrix, the eigenvector of the largest eigenvalue gives each node a score that is high when the node is linked to other well-linked nodes. That is the idea behind eigenvector centrality and PageRank.

## 2. Handout program - inputs and operation
Program: [`code/Task_09_eigenvalues.py`](../code/Task_09_eigenvalues.py)

**Inputs:** A 4-node undirected network (nodes A, B, C, D) as a 4x4 adjacency matrix of 0s and 1s.

**Mathematical operation:** `np.linalg.eig` to get all eigenvalues and eigenvectors, pick the largest eigenvalue, normalise its eigenvector so the scores add up to 1, and check that A v = lambda v.

<details><summary>Output of the handout program</summary>

```text
Original  dominant eigenvalue: 2.5616
  A: 0.2192
  B: 0.2808
  C: 0.2808
  D: 0.2192
  Verification error: 1.9357399876532506e-15

After adding link A-D  eigenvalue: 3.0 scores: [0.25 0.25 0.25 0.25]
After removing link B-C eigenvalue: 2.0 scores: [0.25 0.25 0.25 0.25]
```
</details>

## 3. I changed a parameter
**What I changed:** I added a link between A and D, and in a separate test I removed the link between B and C.

**What happened:** Adding A-D made every node linked to every other node (a complete graph): the dominant eigenvalue rose from 2.5616 to 3.0 and all scores became equal at 0.25. Removing B-C produced a square (4-cycle) where each node has exactly two links: the eigenvalue fell to 2.0 and again every score is 0.25. So the scores become equal when the network is perfectly symmetric.

## 4. What the output means
The dominant eigenvalue is 2.5616. B and C score 0.2808 each, A and D score 0.2192 each. B and C have three links, A and D only two, so B and C are the most influential. The verification error of about 1e-15 shows A v = lambda v holds.


## 5. My own real-world case: Which matatu stage matters most?
Program: [`modified/Task_09_modified_matatu_network.py`](../modified/Task_09_modified_matatu_network.py)

**Assumptions:** A simplified, hypothetical map of 7 Nairobi stages (CBD, Westlands, Kasarani, Rongai, Embakasi, Kikuyu, Eastleigh) where a link means a direct route. These links are invented for practice and do not represent the real network.

**Input data:** A 7x7 symmetric adjacency matrix built from 9 links. I used `np.linalg.eigh` (for symmetric matrices) and also wrote a small power iteration to double-check.

```text
Largest eigenvalue: 3.0704
  CBD        0.2457  (links: 6)
  Eastleigh  0.1677  (links: 3)
  Kasarani   0.1346  (links: 2)
  Embakasi   0.1346  (links: 2)
  Westlands  0.1187  (links: 2)
  Kikuyu     0.1187  (links: 2)
  Rongai     0.0800  (links: 1)
Power-iteration check agrees: True

CBD closed: largest eigenvalue 1.4142 | separate groups of stages: 3
  group 1 : ['Westlands', 'Kikuyu']
  group 2 : ['Kasarani', 'Embakasi', 'Eastleigh']
  group 3 : ['Rongai']
```

**Interpretation:** The largest eigenvalue is 3.07. The CBD has the highest score (0.2457, six links), then Eastleigh (0.1677, three links), and Rongai the lowest (0.0800, one link). The power iteration gave the same scores. When I removed the CBD, the network broke into three separate groups (Westlands-Kikuyu, Kasarani-Embakasi-Eastleigh, and Rongai alone). So the CBD is a single point of failure in this model, and a policy that bans matatus from the CBD would cut off passengers unless there are alternative interchanges.
