#백준 1260: DFS와 BFS


def dfs(c):
    ans_dfs.append(c) # 방문 노드 추가
    v[c] = 1    # 방문 표시

    for n in adj[c]:
        if not v[n]: # 방문하지 않은 노드일 경우
            dfs(n) # dfs 방문

def bfs(s):
    q = [] #변수 생성

    q.append(s) #초기 데이터 삽입
    ans_bfs.append(s)
    v[s] = 1

    while q:
        c = q.pop(0)
        for n in adj[c]:
            if not v[n]:
                q.append(n)
                ans_bfs.append(n)
                v[n] = 1

N,M,V = map(int,input().split())
adj = [[] for _ in range(N+1)]
for _ in range(M):
    s,e = map(int,input().split())
    adj[s].append(e)
    adj[e].append(s)

for i in range(1,N+1):
    adj[i].sort()

v = [0]*(N+1)
ans_dfs = []
dfs(V)

v = [0]*(N+1)
ans_bfs = []
bfs(V)

print(*ans_dfs)
print(*ans_bfs)
