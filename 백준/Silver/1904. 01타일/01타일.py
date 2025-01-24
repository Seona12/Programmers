#첫 번째 줄에 지원이가 만들 수 있는 길이가 N인 모든 2진 수열의 개수를 15746으로 나눈 나머지를 출력한다.
import sys
N = int(sys.stdin.readline())

#이진수 저장할 배열
dp = [0 for _ in range(N+1)]

if N >= 1:
    dp[1] = 1
if N >= 2:
    dp[2] = 2

for i in range(3, N+1):
    dp[i] = (dp[i-1] + dp[i-2]) % 15746

print(dp[N])