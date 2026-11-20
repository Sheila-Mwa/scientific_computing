"""Task 6 (modified): blending 100 kg of dairy-cow feed from three ingredients.
Assumptions (illustrative nutrition values): ingredient 1 = maize germ, 2 = sunflower cake, 3 = fish meal (omena).
Rows: total mass, protein (kg), energy (MJ)."""
import numpy as np

A = np.array([[1.00, 1.00, 1.00],       # kg per kg of ingredient
              [0.09, 0.35, 0.60],       # protein fraction
              [13.0, 10.0, 12.0]])      # MJ of energy per kg
b = np.array([100.0, 21.9, 1200.0])     # targets for the 100 kg batch

x = np.linalg.solve(A, b)
print("kg of maize germ, sunflower cake, fish meal:", np.round(x, 3))
print("All amounts non-negative:", bool(np.all(x >= 0)))
print("Check A @ x:", np.round(A @ x, 6), "| residual norm:", np.linalg.norm(b - A @ x))
print("Condition number:", round(np.linalg.cond(A), 2), "| determinant:", round(np.linalg.det(A), 3))

# Change the protein target to 10 kg: does a valid recipe still exist?
b2 = np.array([100.0, 10.0, 1200.0])
x2 = np.linalg.solve(A, b2)
print("\nProtein target 10 kg ->", np.round(x2, 3), "| all non-negative:", bool(np.all(x2 >= 0)))
