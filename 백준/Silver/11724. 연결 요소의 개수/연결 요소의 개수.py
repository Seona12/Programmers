import sys
sys.setrecursionlimit(10**6)

def dfs(node):
    visited[node] = True  # 현재 노드를 방문 처리
    for neighbor in graph[node]:  # 연결된 모든 노드 탐색
        if not visited[neighbor]:  # 방문하지 않았다면 DFS 재귀 호출
            dfs(neighbor)

# 입력 받기
n, m = map(int, sys.stdin.readline().split())  # 정점 개수, 간선 개수 입력
graph = [[] for _ in range(n + 1)]  # 그래프 인접 리스트 생성
visited = [False] * (n + 1)  # 방문 여부 리스트

# 그래프 구성
for _ in range(m):
    u, v = map(int, sys.stdin.readline().split())
    graph[u].append(v)
    graph[v].append(u)

# 연결 요소 개수 세기
count = 0
for i in range(1, n + 1):
    if not visited[i]:  # 방문하지 않은 노드가 있다면
        dfs(i)  # DFS 탐색 수행
        count += 1  # 연결 요소 개수 증가

print(count)  # 결과 출력
