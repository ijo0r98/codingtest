# 0118

from math import ceil, trunc

# 1 -> 25% 첫번째 숫자는 무조건 포함되어야함
def solution(A, B, K):
    return ceil((B-A)/K) 

# 2 -> 50% 문제 이해를 잘못함
def solution(A, B, K):
    return trunc((B-A)/K) + 1

# 3 -> 37%
def solution(A, B, K):
    for i in range(A, B+1):
        if ((i % K) == 0) and (i != 0):
            return ceil((B-i)/K) 
    return ceil((B-i)/K)  

# 4
def solution(A, B, K):
    for i in range(A, B+1):
        if ((i % K) == 0):
            return B//K - i//K + 1
    return B//K - A//K


# 다른 사람 풀이1
# def solution(A, B, K):
#     return B//K - (A-1)//K

# # 다른 사람 풀이2
# def solution(A, B, K):
#     if (A%K == 0):
#         return B//K - A//K + 1
#     return B//K - A//K 

print(solution(6, 11, 2)) # 3
print(solution(0, 10, 4)) # 3
print(solution(0, 1, 11)) # 1
print(solution(10, 10, 7)) # 0
print(solution(10, 10, 5)) # 1