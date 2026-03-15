import sys

input = sys.stdin.readline

N = int(input())
count, start_index, end_index, sum = 1, 1, 1, 1
while(end_index != N):
	if sum < N:
		end_index+=1
		sum += end_index
	elif sum == N:
	  count += 1
	  end_index += 1
	  sum += end_index
	else:
		sum -= start_index
		start_index += 1

print(count)