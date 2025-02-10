def check_bingo(board):
    bingo_count = 0
    
    # 가로줄 확인
    for row in range(5):
        if all(board[row][col] for col in range(5)):
            bingo_count += 1
            
    # 세로줄 확인
    for col in range(5):
        if all(board[row][col] for row in range(5)):
            bingo_count += 1
            
    # 왼쪽 위 → 오른쪽 아래 대각선
    if all(board[i][i] for i in range(5)):
        bingo_count += 1
    
    # 오른쪽 위 → 왼쪽 아래 대각선
    if all(board[i][4 - i] for i in range(5)):
        bingo_count += 1
        
    return bingo_count >= 3

# 입력 받기
bingo_board = []
num_pos = {}  # {숫자: (row, col)}

for r in range(5):
    row = list(map(int, input().split()))
    bingo_board.append(row)
    for c in range(5):
        num_pos[row[c]] = (r, c)

# 사회자가 부르는 숫자 리스트
call_nums = []
for _ in range(5):
    call_nums.extend(map(int, input().split()))

# 방문 체크 배열
visited = [[False] * 5 for _ in range(5)]

# 사회자가 부르는 숫자를 하나씩 처리
for turn, num in enumerate(call_nums, start=1):
    if num in num_pos:
        r, c = num_pos[num]
        visited[r][c] = True  # 숫자 지우기 (체크)
    
    # 빙고 개수 확인
    if check_bingo(visited):
        print(turn)  # 몇 번째 숫자에서 빙고 발생했는지 출력
        break
