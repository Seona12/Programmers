import sys

def fibonacci(n, memo=None):  
    if memo is None:
        memo = {}  # 새로운 딕셔너리 생성  

    if n <= 1:
        return n  

    if n in memo:  
        return memo[n]  

    memo[n] = fibonacci(n-1, memo) + fibonacci(n-2, memo)  
    return memo[n]

# 입력 받기
n = int(sys.stdin.readline().strip())  # 빠른 입력 사용

# 결과 출력
print(fibonacci(n))
