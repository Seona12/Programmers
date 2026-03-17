from collections import deque

N = int(input())
myQueue = deque()
for i in range(1,N+1):
    myQueue.append(i)
    
while len(myQueue) > 1: #카드가 한 장 남을 때까지
    myQueue.popleft() #카드 하나 버리고
    myQueue.append(myQueue.popleft()) #다음 카드 제일 아래로 옮기기

print(myQueue[0]) #마지막 남은 카드 출력
    