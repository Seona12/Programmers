#연결리스트로 큐 만들기
from collections import deque
import sys

n = int(sys.stdin.readline())
arr = deque([])
for _ in range(n):
    cmd = sys.stdin.readline().split()

    if cmd[0] == 'push':
        arr.append(cmd[1])
    elif cmd[0] == 'pop':
        if len(arr) == 0:
            print(-1)
        else:
            print(arr.popleft())
    elif cmd[0] == 'size':
        print(len(arr))
    elif cmd[0] == 'empty':
        if len(arr) == 0:
            print(1)
        else:
            print(0)
    elif cmd[0] == 'front':
        if len(arr) == 0:
            print(-1)
        else:
            print(arr[0])
    elif cmd[0] == 'back':
        if len(arr) == 0:
            print(-1)
        else:
            print(arr[-1])