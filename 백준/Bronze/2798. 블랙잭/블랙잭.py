from itertools import combinations

def blackjack(N, M, cards):
    max_sum = 0

    # 3장의 카드 조합 생성
    for combo in combinations(cards, 3):
        total = sum(combo)

        # M을 넘지 않는 합 중 최대값 갱신
        if total <= M and total > max_sum:
            max_sum = total

    return max_sum

# 입력 처리
if __name__ == "__main__":
    N, M = map(int, input().split())  # 카드의 개수와 목표 값
    cards = list(map(int, input().split()))  # 카드의 숫자들

    # 결과 출력
    result = blackjack(N, M, cards)
    print(result)