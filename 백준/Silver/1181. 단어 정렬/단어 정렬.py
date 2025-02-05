# 단어정렬
import sys

N = int(input())
arr = []
for i in range(N):
    arr.append(sys.stdin.readline().rstrip())

result = [] # 중복 제거된 값들이 들어갈 리스트

for value in arr:
    if value not in result:
        result.append(value)
        
sorted_arr = sorted(result, key=lambda x: (len(x), x))
for j in range(len(result)):
    print(sorted_arr[j])