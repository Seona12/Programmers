import sys
#상근이가 가지고 있는 숫자 카드의 개수 N
N = int(sys.stdin.readline())
arr1 = list(map(int, sys.stdin.readline().split(' ')))

M = int(sys.stdin.readline())
arr2 = list(map(int,sys.stdin.readline().split(' ')))

card_set = set(arr1)
for i in arr2:
    if i in card_set:
        print(1, end=' ')
    else:
        print(0, end=' ')