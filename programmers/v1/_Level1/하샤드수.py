# 코딩테스트 연습 > 연습문제 > 하샤드 수

# 1
def solution(x):
    sum = 0
    tmp = x
    while tmp != 0:
        sum += tmp % 10
        tmp //= 10

    return x % sum == 0

# 2
def solution(n):
    nsum = sum([int(c) for c in str(n)])
    return n % nsum == 0
    


print(solution(13));