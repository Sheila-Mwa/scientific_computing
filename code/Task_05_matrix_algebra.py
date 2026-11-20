"""Task 5 - Matrix algebra: rotate + scale a square. Parameter change = 90 degree angle and a mirror."""
import numpy as np

points = np.array([[0., 0.], [1., 0.], [1., 1.], [0., 1.]])

def transform(points, angle_deg, sx, sy):
    a = np.deg2rad(angle_deg)
    rotation = np.array([[np.cos(a), -np.sin(a)], [np.sin(a), np.cos(a)]])
    scale = np.array([[sx, 0.], [0., sy]])
    T = rotation @ scale
    return T, points @ T.T

np.set_printoptions(precision=4, suppress=True)
for label, args in (("Original: 45 deg, scale (2, 1.5)", (45, 2.0, 1.5)),
                    ("Change A: 90 deg, scale (2, 1.5)", (90, 2.0, 1.5)),
                    ("Change B: 45 deg, scale (2, -1.5) -> mirror", (45, 2.0, -1.5))):
    T, new = transform(points, *args)
    print(f"\n{label}\nTransformation matrix:\n{T}\nTransformed points:\n{new}")
    print("Determinant:", round(np.linalg.det(T), 4))
