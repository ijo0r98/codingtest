# 0117

# 1 -> 66% 시간복잡도 O(N*M)
def solution(N, A):
    
    answer = [0 for i in range(N)]
    
    max_counter = 0
    for k in range(len(A)):
    #     print(k, answer, max_counter)
        if A[k] == N+1:
            for i in range(N):
                answer[i] = max_counter
        else:
            answer[A[k]-1] += 1
            max_counter = max(answer[A[k]-1], max_counter)
                
    return answer


# 2 -> 11%
def solution(N, A):
    
    answer = [0] * N
    
    max_counter = 0
    cnt = 0
    for k in range(len(A)):
        if A[k] == N+1:
            answer = [0] * N
            cnt += 1
        else:
            answer[A[k]-1] += 1
            max_counter = max(answer[A[k]-1], max_counter)
        
    for i in range(N):
        answer[i] = answer[i] + (max_counter * cnt)
                
    return answer


# 3 -> 22%
def solution(N, A):
    
    answer = [0] * N
    
    max_counter = 0
    tmp = 0
    for k in range(len(A)):
        if A[k] == N+1:
            answer = [0] * N
            if max_counter != 0:
                tmp += max_counter
        else:
            answer[A[k]-1] += 1
            max_counter = max(answer[A[k]-1], max_counter)
    
    for i in range(N):
        answer[i] = answer[i] + tmp
                
    return answer

# 4 -> 77%, timeout error
def solution(N, A):
    answer = [0] * N
    max_counter = 0
    tmp = 0
    for k in range(len(A)):
        if A[k] == N+1:
            answer = [0] * N
            tmp += max_counter
            max_counter = 0
        else:
            answer[A[k]-1] += 1
            max_counter = max(answer[A[k]-1], max_counter)
            
    for i in range(N):
        answer[i] = answer[i] + tmp
                
    return answer

# 5 -> 88%, timeout error
def solution(N, A):
    answer = [0] * N
    max_counter = 0 # 현재 max
    tmp = 0 # 이전의 max
    for k in A:
        if k == N+1:
            answer = [0] * N
            tmp = max_counter
        else:
            answer[k-1] = answer[k-1] + 1
            max_counter = max(answer[k-1] + tmp, max_counter)
            
    for i in range(N):
        answer[i] = tmp + answer[i]
                
    return answer

# 6
def solution(N, A):
    answer = [0] * N
    max_counter = 0 # 현재 max
    tmp = 0 # 이전의 max
    for k in A:
        if k == N+1:
            answer = [max_counter] * N
            tmp = max_counter
        else:
            answer[k-1] += 1
            max_counter = max(answer[k-1], max_counter)
            
    for i in range(N):
        answer[i] = tmp + answer[i]
                
    return answer


# 다른 사람 코드
def solution_(N, A):
    r = N*[0] 	#counter를 담을 리스트
    m1 = 0 	#다음 최댓값이 나오기 전의 최댓값
    m2 = 0 	#for문마다 최댓값
    for i in A:
        if i <= N:
            r[i-1] = max(r[i-1] +1, m1 +1) 	#현재의 최댓값과 counter와 비교
            m2 = max(r[i-1], m2)  #counter와 최댓값과 비교
        else :
            m1 = m2 	#새로운 최댓값으로 업데이트
            
    return [m1 if f < m1 else f for f in r] 	#제일 처음 한번나오고 끝까지 안나온 값을 대비한 for문
        
        
print(solution(1, [2, 1, 1, 2, 1])) # [3]
print(solution(5, [3, 4, 4, 6, 1, 4, 4])) # [3, 2, 2, 4, 2]
print(solution(5, [3, 4, 4, 6, 1, 4, 6])) # [3, 3, 3, 3, 3]
