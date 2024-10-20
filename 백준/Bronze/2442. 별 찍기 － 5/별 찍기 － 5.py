#트리모양으로 별 출력하기
n = int(input())

for i in range(1, n+1):
    print(" " * (n-i)  + '*'* (2*i -1), end = '') # 공백은 n - i 개, 별은 2*i - 1개
    print()  # 줄바꿈