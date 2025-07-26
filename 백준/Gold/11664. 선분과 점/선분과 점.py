import math

def dot(ax, ay, az, bx, by, bz):
    return ax * bx + ay * by + az * bz

def distance(x1, y1, z1, x2, y2, z2):
    return math.sqrt((x1 - x2)**2 + (y1 - y2)**2 + (z1 - z2)**2)

Ax, Ay, Az, Bx, By, Bz, Px, Py, Pz = map(int, input().split())

# Vector AB 
dx = Bx - Ax
dy = By - Ay
dz = Bz - Az

# Vector AP 
px = Px - Ax
py = Py - Ay
pz = Pz - Az

# Squared length of vector AB
ab_squared = dx**2 + dy**2 + dz**2

if ab_squared == 0:
    # A and B are the same point; distance is from A to P
    print(f"{distance(Ax, Ay, Az, Px, Py, Pz):.10f}")
else:
    # Project AP onto AB and calculate the scalar projection (t)
    t = dot(dx, dy, dz, px, py, pz) / ab_squared

    if t < 0:
        closest_x, closest_y, closest_z = Ax, Ay, Az
    elif t > 1:
        closest_x, closest_y, closest_z = Bx, By, Bz
    else:
        # Closest point is on the segment AB
        closest_x = Ax + dx * t
        closest_y = Ay + dy * t
        closest_z = Az + dz * t

    # Compute distance from P to the closest point on the segment (vertical)
    d = distance(Px, Py, Pz, closest_x, closest_y, closest_z) # final output
    print(f"{d:.10f}") 

# This code is highly based on chatgpt-4o (the way used in linear algebra)

# import numpy as np

# # Read input: coordinates of A, B, and P
# Ax, Ay, Az, Bx, By, Bz, Px, Py, Pz = map(int, input().split())

# # Define points as numpy arrays
# A = np.array([Ax, Ay, Az], dtype=np.float64)
# B = np.array([Bx, By, Bz], dtype=np.float64)
# P = np.array([Px, Py, Pz], dtype=np.float64)

# # Vector AB and AP
# AB = B - A  # Direction vector of the segment AB
# AP = P - A  # Vector from A to external point P

# # Squared length of AB
# ab_squared = np.dot(AB, AB)

# if ab_squared == 0:
#     # A and B are the same point; distance is from A to P
#     distance = np.linalg.norm(P - A)
# else:
#     # Project vector AP onto AB to find scalar t
#     t = np.dot(AP, AB) / ab_squared

#     if t < 0:
#         # Closest point is A
#         closest = A
#     elif t > 1:
#         # Closest point is B
#         closest = B
#     else:
#         # Closest point lies between A and B
#         closest = A + t * AB

#     # Compute Euclidean distance from P to the closest point
#     distance = np.linalg.norm(P - closest)

# # Print result with 10 decimal places
# print(f"{distance:.10f}")