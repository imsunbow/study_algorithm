import sys

# no need to set recursion limit cause baekjoon's default recursion depth set to 1000
input = sys.stdin.readline 

def dfs(v):
    trees[v] = -float('inf')
    for i in range(n):
        if v == trees[i]:
            dfs(i)

n = int(input())
trees = list(map(int, input().split()))
tree_to_erase = int(input())

dfs(tree_to_erase)

cnt = 0

for i in range(n):
    if trees[i] != -float('inf') and i not in trees:
        cnt += 1
        
print(cnt)