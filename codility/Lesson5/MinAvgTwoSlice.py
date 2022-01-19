# 0119

# (A[P] + A[P + 1] + ... + A[Q]) / (Q − P + 1), 0 ≤ P < Q < N, notice that the slice contains at least two elements
# return the smallest starting position of such a slice 구간의 평균이 최소일 때 시작하는 인덱스 반환

# 1
def solution(A):
    min_avg = 1000000
    answer = 100000
    for i in range(len(A)-1):
        for j in range(i+1, len(A)):
            tmp = sum(A[i:j+1]) / (abs(i-j)+1)
            if min_avg > tmp:
                min_avg = tmp
                answer = i
    return answer


# 2 -> 60% O(N^2) timeout
def solution(A):
    min_avg = 1000000
    answer = 100000
    for i in range(len(A)-1):
        tmp_sum = A[i]
        for j in range(i+1, len(A)):
            tmp_sum += A[j]
            tmp = tmp_sum / (abs(i-j)+1)
            if min_avg > tmp:
                min_avg = tmp
                answer = i
    return answer

# 3
### 구글링 참고 ###
### a <= b 일때 a < avg(a, b) < b
### a+b <= c+d 일때 (a+b) < avg(a, b, c, d) < (c+d)
# 1 5 3 5 -> (1+5=6) < (3+5=8) -> 6 < avb(6+8)=7 < 8
# 슬라이스 길이가 4개인 경우는 슬라이스 2개인 경우보다 항상 큼, 따라서 신경쓰지 않아도 되며 슬라이스 길이가 2, 3일때만 고려(문제 조건에서 길이 2 이상)

# 3 -> 60%
def solution(A):
    min_avg = 1000000
    answer = 100000
    for i in range(len(A)-1):
        
        # 길이 2
        if min_avg > (A[i]+A[i+1] )/ 2:
            min_avg = ((A[i]+A[i+1]) / 2)
            answer = i
            
        # 길이 3
        if i < len(A)-2:
            if min_avg > (A[i] + A[i+1] + A[i+2]) / 3:
                min_avg = (A[i] + A[i+1] + A[i+2]) / 3
                answer = i
                
    return answer

# 4
# def solution(A):
#     min_value = sum(A[0:2])/2
#     min_index = 0
#     for i in range(len(A)):
#         try:
#             if min_value > (A[1+i] + A[i])/2:
#                 min_value = (A[1+i]+A[i])/2
#                 min_index = i
            
#             if min_value > (A[2+i] + A[1+i] + A[i])/3:
#                 min_value = (A[2+i] + A[1+i] + A[i])/3
#                 min_index = i
#         except:
#             break
    
#     return min_index
    

print(solution([4, 2, 2, 5, 1, 5, 8])) # 1 [2, 2]
print(solution([4, 8, 7, 5, 1, 5, 8])) # 3 [5, 1]
print(solution([5, 6, 3, 4, 9])) # 2
print(solution([10000, -10000])) # 0