from collections import deque
import sys
input = sys.stdin.readline

N,M,Start = map(int,input().split())
#인접 행렬 생성
A = [[] for _ in range(N+1)]

#양방향 그래프 인접행렬에 입력받기
for i in range(M):
    s,e = map(int,input().split())
    A[s].append(e)
    A[e].append(s)

#인접 행렬 오름차순 정렬
for i in range(N+1):
    A[i].sort()
    
def DFS(v):
    print(v, end = " ")
    visited[v] = True
    for i in A[v]:
        if not visited[i]:
            DFS(i)
#매번 방문 배열 초기화
visited = [False] * (N+1)
DFS(Start)

def BFS(v):
    queue = deque()
    queue.append(v)
    visited[v] = True
    while queue:
        now_Node = queue.popleft()
        print(now_Node, end = ' ')
        for i in A[now_Node]:
            if not visited[i]:
                visited[i] = True
                queue.append(i)
                
                
print() 
#매번 방문 배열 초기화
visited = [False] * (N+1)
BFS(Start)
    
