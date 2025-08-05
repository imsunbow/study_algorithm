from itertools import permutations

n = int(input())
lst = [i for i in range(1, n + 1)]

for perm in permutations(lst):
    print(' '.join(map(str, perm)))