#백준 2667: 단지번호붙이기

#dfs
def dfs(x, y):
    global count #global variable
    if x<=-1 or x>=n or y<=-1 or y>=n: #out of range
        return False 

    if graph[x][y] == 1: #not visited
        graph[x][y] = 0
        count += 1
        dfs(x-1, y)
        dfs(x+1, y)
        dfs(x, y-1)
        dfs(x, y+1)
        return True
    return False

n = int(input())
graph = []

for i in range(n):
    graph.append(list(map(int, input())))
    
result = 0

count = 0
count_list = []

for i in range(n):
    for j in range(n):
        if dfs(i, j) == True:
            result += 1
            count_list.append(count)
            count = 0
            
print(result)

#cnt_list sort & print
count_list.sort()
for i in count_list:
    print(i)
    