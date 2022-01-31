# 코딩테스트 연습 > 연습문제 > N개의 최소공배수

def solution(arr):
    answer = 1
    while(arr):
        num = arr.pop()
        answer = lcd(num, answer)

    return int(answer)

# 최대공약수(유클리드 호제법)
def gcd(n, m):
    while m != 0:
        n, m = m, n%m
    return n

# 최소공배수
def lcd(n, m):
    return n * m / gcd(n, m)


print('answer: ', solution([2,6,8,14])) # 168
print('answer: ', solution([1, 2 ,3])) # 168

