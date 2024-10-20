n = int(input())

for i in range(1, n + 1):
    # 공백은 i-1개, 별은 2 * (n - i + 1) - 1개 출력
    print(" " * (i - 1) + '*' * (2 * (n - i + 1) - 1))
for j in range(2, n + 1):
    print(" " * (n - j) + '*' * (2 * j - 1)) 