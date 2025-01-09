import sys
hap = 0
n = int(sys.stdin.readline().rstrip())

for i in range(n):
    hap += i+1
    i+=1
print(hap)