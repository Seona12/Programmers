import sys

class Stack:
    def __init__(self):
        self.stack =[]
    
    #push X: 정수 X를 스택에 넣는 연산이다.
    def push_X(self, x):
        self.stack.append(x)
    
    #pop: 스택에서 가장 위에 있는 정수를 빼고, 그 수를 출력한다. 만약 스택에 들어있는 정수가 없는 경우에는 -1을 출력한다.
    def pop(self):
        if self.stack:
            return self.stack.pop()
        else:
            return -1
        
    #top: 스택의 가장 위에 있는 정수를 출력한다. 만약 스택에 들어있는 정수가 없는 경우에는 -1을 출력한다.
    def top(self):
        if self.stack:
            return self.stack[-1]
        else:
            return -1
    
    #size: 스택에 들어있는 정수의 개수를 출력한다.
    def size(self):
        return len(self.stack)
    
    #empty: 스택이 비어있으면 1, 아니면 0을 출력한다.
    def is_empty(self):
        if self.stack:
            return 0
        else:
            return 1


if __name__ == '__main__':
    n = int(sys.stdin.readline().strip())
    s = Stack() #스택 생성
    
    for _ in range(n):
        cmd = sys.stdin.readline().split() #명령어 입력
        if cmd[0] == 'push':
            s.push_X(cmd[1])
        elif cmd[0] == 'top':
            print(s.top())
        elif cmd[0] == 'size':
            print(s.size())
        elif cmd[0] == 'empty':
            print(s.is_empty())
        elif cmd[0] == 'pop':
            print(s.pop())
        