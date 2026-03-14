import sys
input = sys.stdin.readline
n,m = map(int, input().split())
A = [[0] * (n+1)]#원본 리스트 : 1차원 배열(0으로 초기화)
D = [[0]*(n+10) for _ in range(n+1)] #합배열 : 2차원 배열(0으로 초기화)

# 원본 배열 입력받아 저장하기
for i in range(n):
    A_row = [0] + [int(x) for x in input().split()] #블럭마냥 쌓기
    A.append(A_row)

# 합 배열 구하기
for i in range(1,n+1):
    for j in range(1,n+1):
        D[i][j] = D[i][j-1] + D[i-1][j] - D[i-1][j-1] + A[i][j]

# 구간합 배열로 질의에 대한 답 구하기
for i in range(m):
    x1,y1,x2,y2 = map(int,input().split())
    result = D[x2][y2] - D[x1-1][y2] - D[x2][y1-1] + D[x1-1][y1-1]
    print(result)