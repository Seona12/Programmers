import sys
input = sys.stdin.readline

N = int(input())
arr = [0] * N
end_result = []
for i in range(N):
    arr[i] = int(input())

def mergesort(arr):
    if len(arr) <= 1:
        return arr
    else:
        mid = len(arr) // 2
        left = mergesort(arr[:mid])
        right = mergesort(arr[mid:])
        return merge(left,right)

def merge(left,right):
    result = []
    i = 0
    j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    while i < len(left):
        result.append(left[i])
        i += 1
    while j < len(right):
        result.append(right[j])
        j += 1
    return result

end_result = mergesort(arr)
for i in range(N):
    print(end_result[i])