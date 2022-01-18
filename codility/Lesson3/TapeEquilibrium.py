# 0114

# 1 -> 46% 시간복잡도 O(n^2)
def solution(A):
    min_sum = 100
    for i in range(1, len(A)):
        tmp = abs(sum(A[:i]) - sum(A[i:]))
        min_sum = min(min_sum, tmp)
    return min_sum

# 2 -> 15% left, right 초기값이랑 반복문 i 잘못 설정
def solution(A):
    min_sum = 100
    left = 0
    right = sum(A)
    for i in range(1, len(A)):
        left += A[i]
        right -= A[i]
        min_sum = min(min_sum, abs(left-right))
    return min_sum

# 3 -> 69% 마지막 원소 하나 남는 경우 생각 안함 & min_sum 초기값 잘못 설정
def solution(A):
    min_sum = 100
    left = 0
    right = sum(A)
    for i in range(len(A)):
        left += A[i]
        right -= A[i]
        min_sum = min(min_sum, abs(left-right))
    return min_sum

# 4 -> 100 %
def solution(A):
    min_sum = 100000
    left = 0
    right = sum(A)
    for p in range(len(A)-1):
        left += A[p]
        right -= A[p]
        min_sum = min(min_sum, abs(left-right))
    return min_sum

# print(solution([3, 1, 2, 4, 3])) # 1
# print(solution([3, 4])) # 1
# print(solution([1, 1, 3])) # 1
print(solution([-1000, 1000])) # 1