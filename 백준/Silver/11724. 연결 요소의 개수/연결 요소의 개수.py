#백준 11724: 연결 요소의 개수

import sys
n,m = map(int,sys.stdin.readline().split())
graph = {}

#그래프 입력
for _ in range(m):
    u,v = map(int,sys.stdin.readline().split())
    if u in graph:
        graph[u].append(v)
    else:
        graph[u] = [v]

    if v in graph:
        graph[v].append(u)
    else:
        graph[v] = [u]

#dfs 함수 설정
def dfs(u):
    visited[u] = True
    if u in graph:
        for v in graph[u]:
            if visited[v] == False:
                dfs(v)

#초기화(방문,cnt)
visited= [False for _ in range(n+1)]
cnt = 0


for u in range(1,n+1):
    #방문 기록이 있으면 cnt값 증가
    if visited[u] == False:
        dfs(u)
        cnt += 1

#출력
print(cnt)
