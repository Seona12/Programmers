import sys
N = int(input())
list_one = list(map(int,sys.stdin.readline().split()))

max_num = max(list_one)
min_num = min(list_one)

print(min_num, max_num)