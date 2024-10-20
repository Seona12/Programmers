n = int(input())

for i in range(1, n+1):  # 바깥 for문은 줄 번호
    for j in range(i):     # 안쪽 for문은 각 줄에 출력할 별 개수
        print('*', end='')
    print()  # 줄바꿈