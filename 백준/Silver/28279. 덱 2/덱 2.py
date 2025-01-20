from collections import deque
import sys

deq = deque()

# 1: 정수 X를 덱의 앞에 넣는다.
def X_one(X):
    deq.appendleft(X)

# 2: 정수 X를 덱의 뒤에 넣는다.
def X_two(X):
    deq.append(X)

# 3: 덱의 가장 앞에 있는 수를 뺀다.
def three():
    if len(deq) == 0:
        print(-1)
    else:
        print(deq.popleft())

# 4: 덱의 가장 뒤에 있는 수를 뺀다.
def four():
    if len(deq) == 0:
        print(-1)
    else:
        print(deq.pop())

# 5: 덱에 들어있는 정수의 개수를 출력한다.
def five():
    print(len(deq))

# 6: 덱이 비어있으면 1을, 아니면 0을 출력한다.
def six():
    if len(deq) == 0:
        print(1)
    else:
        print(0)

# 7: 덱의 가장 앞에 있는 수를 출력한다.
def seven():
    if len(deq) == 0:
        print(-1)
    else:
        print(deq[0])

# 8: 덱의 가장 뒤에 있는 수를 출력한다.
def eight():
    if len(deq) == 0:
        print(-1)
    else:
        print(deq[-1])

# 명령 처리 루프
n = int(sys.stdin.readline())
for _ in range(n):
    cmd = sys.stdin.readline().split()
    if cmd[0] == '1':
        X_one(int(cmd[1]))
    elif cmd[0] == '2':
        X_two(int(cmd[1]))
    elif cmd[0] == '3':
        three()
    elif cmd[0] == '4':
        four()
    elif cmd[0] == '5':
        five()
    elif cmd[0] == '6':
        six()
    elif cmd[0] == '7':
        seven()
    elif cmd[0] == '8':
        eight()
