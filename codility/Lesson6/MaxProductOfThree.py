# 0120

# 3개의 원소 곱해서 가장 큰 수 반환

# 1 -> 100%
def solution(A):
    A = sorted(A, reverse=True) # 내림차순 정렬

    if (A[2] > 0) or (A[0] < 0): # + + +, - - -
        answer = (A[0] * A[1] * A[2])
        # - - * 가 더 큰 경우
        answer = max(answer, A[-1] * A[-2] * A[0])
    elif (A[2] < 0) and (A[1] > 0): # + + - -> + - -
        answer = (A[0] * A[-1] * A[-2])
    elif (A[1] < 0): # + - -
        answer = (A[0] * A[-1] * A[-2])
            
    return answer
    
    
# 2 간단한 버전
def solution(A):
    A = sorted(A, reverse=True) # A.sort()
    return max((A[0]*A[1]*A[2]), (A[0]* A[-1]* A[-2]))

print(solution([-3, 1, 2, -2, 5, 6])) # 60
print(solution([1, 2, 3, 4, 5])) # 60
print(solution([1, 2, -3, -4, -5])) # 40
print(solution([1, -2, -3, -4, -5])) # 20
print(solution([-4, -6, 3, 4, 5])) # 120