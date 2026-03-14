import sys
input = sys.stdin.readline
N,M = map(int, input().split())
numbers = list(map(int,input().split()))
prefix_sum = [0]

temp = 0

for i in numbers:
    temp += i
    prefix_sum.append(temp) #합 배열

for e in range(M):
    i,j = map(int, input().split())
    print(prefix_sum[j] - prefix_sum[i-1]) #합배열에서 구간합 구하기
