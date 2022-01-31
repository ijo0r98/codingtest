# 코딩테스트 연습 > 연습문제 > 정수 제곱근 판별

def solution(n):
    if (n**(1/2)) % 1 == 0:
        k = int(n**(1/2))
        return (k+1)**2
    return -1

def solution(n):
    return -1 if (n**(1/2)) % 1 != 0 else (int(n**(1/2))+1) ** 2
    


print(solution(121)) # 144
print(solution(3)) # -1
