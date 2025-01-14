n = int(input())

sorted_list = sorted([int(input()) for _ in range(n)])

for i in range(n):
    print(sorted_list[i])
    i+=1