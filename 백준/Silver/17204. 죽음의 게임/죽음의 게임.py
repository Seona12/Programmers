from collections import deque

def bfs(N, K, targets):
    queue = deque([(0, 1)])  # (현재 번호, 카운트)
    visited = set()          # 방문한 노드 체크

    while queue:
        current, count = queue.popleft()

        # 다음 지목된 사람이 누구인지 확인
        next_person = targets[current]

        # 보성이가 걸린 경우
        if next_person == K:
            return count

        # 방문하지 않은 경우에만 진행
        if next_person not in visited:
            visited.add(next_person)
            queue.append((next_person, count + 1))

    return -1  # 어떤 방법으로도 보성이 걸리지 않는 경우

# 입력 처리
N, K = map(int, input().split())
targets = [int(input()) for _ in range(N)]

# 결과 출력
print(bfs(N, K, targets))
