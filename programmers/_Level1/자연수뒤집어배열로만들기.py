# 코딩테스트 연습 > 연습문제 > 자연수 뒤집어 배열로 만들기

def solution(n):
    answer = [int(i) for i in str(n)]
    answer.reverse()
    return answer


def solution(n):
    return list(map(int, reversed(str(n))))

def solution(n):
    return [int(i) for i in str(n)][::-1]


print(solution(12345)) # [5,4,3,2,1]