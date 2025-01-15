# 입력값을 리스트로 저장
numbers = [int(input()) for _ in range(5)]

# 평균 계산
def calculate_mean(nums):
    return sum(nums) // len(nums)

# 중앙값 계산
def calculate_median(nums):
    sorted_nums = sorted(nums)
    return sorted_nums[len(sorted_nums) // 2]

# 평균과 중앙값 계산
mean = calculate_mean(numbers)
median = calculate_median(numbers)

# 결과 출력
print(mean)
print(median)