N = int(input())
mylist = list(map(int, input().split()))

max_list = max(mylist)
sum_list = sum(mylist)

print(sum_list*100/max_list/N)