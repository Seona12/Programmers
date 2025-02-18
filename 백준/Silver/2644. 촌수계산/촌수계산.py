from collections import deque

def bfs(graph, start, target, n):
    visited = [-1] * (n + 1)
    queue = deque([(start, 0)])
    visited[start] = 0
    
    while queue:
        node, degree = queue.popleft()
        if node == target:
            return degree
        
        for neighbor in graph[node]:
            if visited[neighbor] == -1:
                queue.append((neighbor, degree + 1))
                visited[neighbor] = degree + 1
    
    return -1

n = int(input())
x, y = map(int, input().split())
m = int(input())

graph = {i: [] for i in range(1, n+1)}
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

print(bfs(graph, x, y, n))