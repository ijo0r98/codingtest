# 코딩테스트 연습 > 연습문제 > 최대공약수와 최소공배수

def solution(n, m):
    answer = []
    answer.append(gcd2(n, m))
    answer.append(lcd(n, m, answer[0]))
        
    return answer

# 최대공약수(for문 이용)
def gcd1(n, m):
    for i in range(min(n, m), 0, -1):
        if (n%i == 0) & (m%i == 0):
            return i

# 최대공약수(유클리드 호제법)
def gcd2(n, m):
    # n과 m으로 나눈 나머지와 m의 최대공약수 == n과 m의 최대공약수
    # n에는 m을, m에는 n을 m으로 나눈 나머지를  m이 0이 될 때까지 대입시켜 반복하면 남는 n값이 최대공약수
    while m != 0:
        n, m = m, n%m
    return n

# 최소공배수
def lcd(n, m, gcd):
    return n * m / gcd


print(solution(3, 12)) # [3, 12]
print(solution(2, 5)) # [1, 10]