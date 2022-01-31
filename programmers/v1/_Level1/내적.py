# 코딩테스트 연습 > 월간 코드 챌린지 시즌1 > 내적

# 1
def solution(a, b):
    answer = 0
    # answer = answer + (ai * bi) for a1, b1 in zip(a, b)
    for i in range(len(a)):
        answer += a[i] * b[i]
    return answer

# 2
def solution(a, b):
    return sum([x * y for x, y in zip(a, b)])


print(solution([1,2,3,4], [-3,-1,0,2])) # 3