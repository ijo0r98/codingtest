# 0114

# 1 -> 50%
# def solution(A):
#     A = sorted(A) # n*logN
#     for i in range(len(A)-1):
#         if (A[i+1]-A[i]) != 1:
#             return A[i]+1
#     return A[-1]+1

# # 2 빈 리스트 입력 시 해결 -> 60% 
# def solution(A):
#     if not A:
#         return 1
#     A = sorted(A) # n*logN
#     for i in range(len(A)-1):
#         if (A[i+1]-A[i]) != 1:
#             return A[i]+1
#     return A[-1]+1

# 3 첫 시작이 1이 아닐 때 -> 100%
def solution(A):
    if not A:
        return 1
    A = sorted(A) # n*logN
    if A[0] != 1:
        return 1
    for i in range(len(A)-1):
        if (A[i+1]-A[i]) != 1:
            return A[i]+1
    return A[-1]+1
    
    
    
print(solution([1, 2, 5, 3]))
print(solution([1]))    
print(solution([1, 3]))
print(solution([2, 3]))