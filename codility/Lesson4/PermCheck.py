# 0117

def solution(A):
    # permutation 순열
    A = sorted(A)
    if (A[0] != 1) or (A[-1] != len(A)):
        return 0
    for i in range(len(A)-1):
        if (A[i+1]-A[i]) != 1:
            return 0
    
    return 1

print(solution([4, 1, 3, 2])) # 1
print(solution([4, 1, 3])) # 0
print(solution([1, 3, 3])) # 0
print(solution([1, 2, 3, 3])) # 0
print(solution([1, 2, 3])) # 1
    