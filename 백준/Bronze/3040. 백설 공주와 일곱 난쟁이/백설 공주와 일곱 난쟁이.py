#백준 3040: 백설공주와 일곱 난쟁이

from itertools import combinations
import sys
input = sys.stdin.readline

dwarfs_list = [int(input()) for _ in range(9)]

case = list(combinations(dwarfs_list,7))

for i in case:
    if sum(i) == 100:
        for j in i:
            print(j)