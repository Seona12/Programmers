import sys
sys.setrecursionlimit(10000)
input = sys.stdin.readline

N,M = map(int,input().split())
#인접리스트 a 초기화
A = [[] for _ in range(N+1)]
#방문 배열 visited 초기화
visited = [False] * (N+1)

for i in range(M):
    u,v = map(int,input().split())
    A[u].append(v)
    A[v].append(u)

def DFS(v):
    visited[v] = True
    for i in A[v]:
        if not visited[i]:
            DFS(i)

count = 0

for i in range(1,N+1):
    if not visited[i]:
        count += 1
        DFS(i)

print(count)
    