pieces = list(map(int, input().split()))

while pieces != [1, 2, 3, 4, 5]:  # 정렬될 때까지 반복
    for i in range(4):  # 연속된 두 개를 비교
        if pieces[i] > pieces[i + 1]:  # 앞 숫자가 크다면 swap
            pieces[i], pieces[i + 1] = pieces[i + 1], pieces[i]
            print(*pieces)  # 리스트 상태 출력
