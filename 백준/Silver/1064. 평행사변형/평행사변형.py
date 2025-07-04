# 백준 1064: 평행사변형

# Given three points, find the difference between the maximum and minimum possible parallelogram perimeters.
# If the three points are collinear, print -1.

import sys
input = sys.stdin.readline

XA, YA, XB, YB, XC, YC = map(int, input().split())

def distance(x1, y1, x2, y2):
    # Returns the Euclidean distance between two points
    return ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5

answer = 0.0

# Check if all x or all y are the same (vertical or horizontal line)
if XA == XB == XC or YA == YB == YC:
    answer = -1.0
# Check if the three points are collinear using slope comparison (avoid division by zero)
elif (XA-XB)*(YA-YC) == (XA-XC)*(YA-YB):
    answer = -1.0
else:
    dAB = distance(XA, YA, XB, YB)
    dBC = distance(XB, YB, XC, YC)
    dCA = distance(XC, YC, XA, YA)
    answer = (max(dAB, dBC, dCA) - min(dAB, dBC, dCA)) * 2

print(answer)