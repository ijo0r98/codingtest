# 코딩테스트 연습 > 연습문제 > 숫자의 표현

def solution(n):
    answer = 1
    tmp = n
    for i in range(1, n):
        j = i
        tmp = n - i
        while tmp > 0:
            j += 1
            tmp -= j

        if tmp == 0:
            answer += 1

    return answer


print(solution(15)) # 4