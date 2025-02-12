import sys

def charge(k,n):
    dp = [[0] * (n+1) for _ in range(k+1)]
    #0층
    for i in range(1, n+1):
        dp[0][i] = i
    
    #테이블 채우기
    for floor in range(1, k+1):
        for room in range(1, n+1):
            dp[floor][room] = dp[floor][room-1] + dp[floor-1][room]
    return dp[k][n]
one = int(sys.stdin.readline().rstrip())
for _ in range(one):
    name_one = int(sys.stdin.readline().rstrip())
    name_two = int(sys.stdin.readline().rstrip())
    print(charge(name_one,name_two))
