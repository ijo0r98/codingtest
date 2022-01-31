# 코딩테스트 연습 > 월간 코드 챌린지 시즌3 > 없는 숫자 더하기

# 내 코드 1 
def solution(numbers):
    answer = 0
    for i in range(10):
        if i not in numbers:
            answer += i
    return answer


# 내 코드 2 - 집합
def solution(numbers):
    nums = set(range(1, 10))
    numsD = nums - set(numbers)
    return sum(numsD)


# 다른 사람 풀이 1
def solution(numbers):
    return 45 - sum(numbers)



print(solution([1,2,3,4,6,7,8,0])) # 14