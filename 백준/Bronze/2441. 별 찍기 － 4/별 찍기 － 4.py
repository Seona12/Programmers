n = int(input())

for i in range(n, 0 , -1):  # 바깥 for문은 줄 번호
    print( " " *(n-i) + '*'* i , end='')
    print()  # 줄바꿈