import sys
input = sys.stdin.read  
data = input().splitlines()  

T = int(data[0])

result = []
for i in range(1, T + 1):
    a, b = map(int, data[i].split())
    result.append(a + b)

# 출력하기
sys.stdout.write('\n'.join(map(str, result)) + '\n')
