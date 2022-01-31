# 코딩테스트 연습 > 연습문제 > x만큼 간격이 있는 n개의 숫자

def solution(x, n):
    answer = []
    for i in range(1, n+1):
        answer.append(x * i)
    return answer

def solution(x, n):
    return [i * x for i in range(1, n + 1)]


print(solution(2, 5))