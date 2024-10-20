n = int(input())  # N 입력받기

# 위쪽 부분 출력
for i in range(1, n):
    print("*" * i + ' ' * (2 * (n - i)) + "*" * i)

# 중간 부분 출력
print("*" * (2 * n))

# 아래쪽 부분 출력
for i in range(n - 1, 0, -1):
    print("*" * i + ' ' * (2 * (n - i)) + "*" * i)
