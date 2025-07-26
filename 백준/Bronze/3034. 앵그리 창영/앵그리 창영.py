import math

n, w, h = map(int, input().split())

for _ in range(n):
    len = int(input())
    print("DA" if len <= math.sqrt(w ** 2 + h **2) else "NE")   
    # if len <= math.sqrt(w ** 2 + h ** 2):
    #     print("DA")
    # else:
    #     print("NE")