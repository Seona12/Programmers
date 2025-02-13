def precompute_combinations(max_n, max_m):
    """ DP를 사용하여 조합을 미리 계산하는 함수 """
    dp = [[0] * (max_m + 1) for _ in range(max_n + 1)]

    # 초기값 설정
    for i in range(max_m + 1):
        dp[0][i] = 1  # N = 0일 때, 아무 다리도 놓지 않는 경우는 1가지

    # DP 테이블 채우기
    for n in range(1, max_n + 1):
        for m in range(n, max_m + 1):  # m >= n 조건 유지
            dp[n][m] = dp[n-1][m-1] + dp[n][m-1]

    return dp

# 최대 N, M이 29이므로 미리 DP 계산
MAX_N, MAX_M = 29, 29
dp_table = precompute_combinations(MAX_N, MAX_M)

# 입력 및 실행
T = int(input())  # 테스트 케이스 개수
for _ in range(T):
    N, M = map(int, input().split())
    print(dp_table[N][M])  # 미리 계산된 DP 테이블에서 정답 출력
