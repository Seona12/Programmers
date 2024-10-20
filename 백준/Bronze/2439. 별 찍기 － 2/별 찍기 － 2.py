#별찍기 2
n = int(input())
for i in range(1, n+1):  # 바깥 for문은 줄 번호
    print(" " * (n-i) + "*" * (i), end = "")
    print()