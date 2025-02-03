list_a = []

for _ in range(9):
    list_a.append(int(input()))

total = sum(list_a)  # 아홉 난쟁이 키의 합

# 두 명을 찾아서 제외
found = False
for i in range(9):
    for j in range(i + 1, 9):
        if total - (list_a[i] + list_a[j]) == 100:
            fake1, fake2 = list_a[i], list_a[j]
            found = True
            break
    if found:
        break

# 두 명 제거 후 출력
list_a.remove(fake1)
list_a.remove(fake2)
list_a.sort()

for height in list_a:
    print(height)
