# 입력 받기
import sys
input = sys.stdin.read
data = input().splitlines()

# 첫 줄: 영수증에 적힌 총 금액
X = int(data[0])

# 둘째 줄: 구매한 물건의 종류 수
N = int(data[1])

calculated_total = 0
for i in range(2, 2 + N):
    a, b = map(int, data[i].split())
    calculated_total += a * b

# 결과 비교 후 출력
if calculated_total == X:
    print("Yes")
else:
    print("No")
