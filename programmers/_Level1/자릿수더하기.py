# 코딩테스트 연습 > 연습문제 > 자릿수 더하기

def solution(n):
    answer = 0
    while n != 0:
        answer += n % 10
        n //= 10 

    return answer


def solution(number):
    return sum([int(n) for n in str(number)])