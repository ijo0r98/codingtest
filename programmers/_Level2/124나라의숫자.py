# 코딩테스트 연습 > 연습문제 > 124 나라의 숫자

# 1, 2, 4, 11, 12, 14, 21, 22, 24, 41, 42, 44, 111, 112, 114, 121, ...
# 1, 2, 3,  4,  5,  6,  7,  8,  9, 10, 11, 12,  13,  14,  15,  16, ...

# 내 풀이
def solution(n):

    answer = ''
    while n > 0:
        print(n)
        if n % 3 == 1:
            answer += '1'
        elif n % 3 == 2:
            answer += '2'
        else:    
            answer += '4'

        n = n // 3 

    return answer[::-1]  # 순서 반대로 출력


# 다른 사람 풀이 1
def solution(n):
    result = []
    while n:
        t = n % 3
        if not t:
            t = 3
            n -= 1
        result.append(str(t))
        n //= 3
        
    for i in range(len(result)):
        if result[i] == '3':
            result[i] = '4'
    return ''.join(result[::-1])

# 다른 사람 풀이 2
def solution(n):
    answer = ''
    while n > 0:
        n -= 1
        answer = '124'[n % 3] + answer
        n //= 3

    return answer
    
