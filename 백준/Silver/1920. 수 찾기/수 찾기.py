import sys

N = int(sys.stdin.readline())
list_one = set(map(int, sys.stdin.readline().split()))

M = int(sys.stdin.readline())
list_two = list(map(int, sys.stdin.readline().split()))

for x in list_two:
    if x in list_one:  # 리스트 A에서 x가 존재하는지 확인
        print(1)
    else:
        print(0)
