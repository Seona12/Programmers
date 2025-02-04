#나이순 정렬

#온라인 저지 회원의 수 N
N = int(input())
list_1 = []
for i in range(N):
    age, name = input().split()
    list_1.append((int(age), name))
    
#나이순 정렬
list_1.sort(key = lambda x: x[0])

for age, name in list_1:
    print(age, name)