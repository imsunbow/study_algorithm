#백준 15640: n과 m

from itertools import combinations
import sys

def print_combination(n,m):
    numbers = list(range(1,n+1))
    comb = combinations(numbers,m)

    for c in comb:
        print(" ".join(map(str,c)))


n,m = map(int,sys.stdin.readline().split())
print_combination(n,m)