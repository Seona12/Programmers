# 입력 받기
word = input().strip()

# 스택에 문자 추가
stack = list(word)  # 단어를 문자로 쪼개 스택처럼 사용

# 팰린드롬 확인
is_palindrome = True
for char in word:  # 단어의 각 문자와 스택의 LIFO 순서 비교
    if char != stack.pop():
        is_palindrome = False
        break

# 결과 출력
print(1 if is_palindrome else 0)
