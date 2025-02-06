import sys
from datetime import datetime

N = int(input())  # 학생 수 입력

students = []

for _ in range(N):
    data = sys.stdin.readline().split()  # 공백 기준으로 나누기
    name = data[0]  # 이름
    day, month, year = map(int, data[1:])  # 날짜 숫자로 변환
    birthdate = datetime(year, month, day)  # 날짜 객체 생성
    students.append((birthdate, name))  # 리스트에 (생일, 이름) 저장

# 날짜 기준 정렬 (자동 오름차순 정렬)
students.sort()

# 출력
print(students[-1][1])  # 가장 나이 적은 사람
print(students[0][1])  # 가장 나이 많은 사람
