import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
N = int(input())

def isPrime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True
def DFS(number):
    if len(str(number)) == N:
        print(number)
        return
    for i in [1,3,5,7,9]:
        next_number = number * 10 + i
        if isPrime(next_number):
            DFS(next_number)
DFS(2)
DFS(3)
DFS(5)
DFS(7)