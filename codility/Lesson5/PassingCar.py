# 0118

# 0 동쪽으로 이동하는 차 P
# 1 서쪽으로 이동하는 차 Q
# P, Q가 서로 지나칠 때 (P, Q)쌍의 수를 구하여라
# P < Q P(0)가 먼저 등장한 뒤 나오는 Q(1)만 고려

# 1 
def solution(A):
    answer = 0
    p_list = []
    
    for i in range(len(A)):
        if A[i] == 0:
            p_list.append(i)
        else:
            answer += len(p_list)
    
    return -1 if answer > 1000000000 else answer


print(solution([0, 1, 0, 1, 1]))
print(solution([0, 1, 0, 1]))
print(solution([1, 0, 0, 0]))
print(solution([1, 0, 0, 0, 1]))