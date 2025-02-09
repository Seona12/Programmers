import sys

N = int(input())
people = [tuple(map(int, sys.stdin.readline().split())) for _ in range(N)]

ranks = []
for i in range(N):
    rank = 1  # 기본 등수
    for j in range(N):
        if i != j and people[j][0] > people[i][0] and people[j][1] > people[i][1]:
            rank += 1  # 자신보다 덩치가 큰 사람이 있으면 등수 증가
    ranks.append(rank)

print(" ".join(map(str, ranks)))