#다이아몬드 모양으로 별 출력하기
n = int(input())

for j in range(1, n+1):
    print(" " * (n-j) + "*" * (2*j-1), end = '')
    print()
    
for i in range(n-1, 0, -1):
    print(" " * (n-i)  + '*'* (2*i -1), end = '') 
    print()