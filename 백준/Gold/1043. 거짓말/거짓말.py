# 백준 1043: 거짓말

# solve 1
# import sys
# input = sys.stdin.readline

# n,m = map(int, input().split())
# know = set(input().split()[1:]) 
# people = []

# for _ in range(m):
#     people.append(set(input().split()[1:])) # append the list of people who are at each party


# # count the number of people who knows I'm lying
# for _ in range(m):
#     for person in people:
#         if person & know: # if person knows someone who is lying
#             know = know.union(person) # add them to the set of liars

# cnt = 0
# for person in people:
#     if person & know: # if no one at the party knows a liar
#         continue 
#     cnt += 1


# print(cnt)

# solve 2

# 1. Use union-find to group people who are connected by attending the same party 
# 2. Identify root groups that contain people who know the truth.
# 3. Count parties where no attendee belongs to a truth-knowing group.

import sys
input = sys.stdin.readline

# Find the root parent of x with path compression
def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

# Union the groups of x and y
def union(x, y):
    x_root = find(x)
    y_root = find(y)
    if x_root != y_root:
        parent[y_root] = x_root

n, m = map(int, input().split())
truth = set(map(int, input().split()[1:]))  # People who know the truth

parent = list(range(n + 1))  # Union-find parent array (1-based index)
parties = []

# Read all party data and union all people in the same party
for _ in range(m):
    party = list(map(int, input().split()))[1:]
    for i in range(len(party) - 1):
        union(party[i], party[i + 1])
    parties.append(party)

# Get the set of root parents for people who know the truth
truth_roots = set(find(p) for p in truth)

# Count parties where no one is connected to any truth-knower
ans = 0
for party in parties:
    if all(find(p) not in truth_roots for p in party):
        ans += 1

print(ans)
