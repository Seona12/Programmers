import sys

input = sys.stdin.readline

N = int(input())
A = []

for i in range(N):
    A.append((int(input()),i))
    
MAX = 0    
sort_A = sorted(A)

for i in range(N):
    if MAX < sort_A[i][1]-i:
        MAX = sort_A[i][1]-i

print(MAX+1)