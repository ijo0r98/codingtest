# 0114
# 1차 100%

def solution(A, K):
    length = len(A)
    answer = [0 for i in range(length)]
    for i in range(len(A)):
        new_i = (i + K) % length
        answer[new_i] = A[i]
    
    return answer
    
    
print(solution([3, 8, 9, 7, 6], 3)) # [9, 7, 6, 3, 8]