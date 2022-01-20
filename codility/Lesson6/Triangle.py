# 0120

# 삼각형을 이루는 세 변이 주어지는지 확인

def solution(A):
    A.sort(reverse=True)
    for i in range(len(A)):
        try:
            if A[i] < A[i+1] + A[i+2]:
                return 1
        except:
            break
    return 0
    
    
print(solution([10, 2, 5, 1, 8, 20])) # 1
print(solution([10, 2, 5, 1])) # 0
