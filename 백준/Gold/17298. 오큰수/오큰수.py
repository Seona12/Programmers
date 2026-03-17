import sys
input = sys.stdin.readline

N = int(input())
ans = [0] * N
A = list(map(int,input().split()))
myStack = []

for i in range(N):
    while myStack and A[myStack[-1]] < A[i]: #오큰수 맞음
        ans[myStack.pop()] = A[i] #정답리스트에 오큰수 저장하기
    myStack.append(i)
while myStack:
    ans[myStack.pop()] = -1

result = ""

print(*ans)