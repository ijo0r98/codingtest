# 코딩테스트 연습 > Summer/Winter Coding(~2018) > 소수 만들기

def solution(nums):
    answer = 0
    temp = 0
    length = len(nums)
    for i in range(length):
        for j in range(i+1, length):
            for k in range(j+1, length):
                temp = nums[i] + nums[j] + nums[k]
                for l in range(2, temp):
                    if temp % l == 0:
                        break
                    if l == temp-1:
                        answer += 1

    return answer


# 다른 사람 풀이 
from itertools import combinations 

def solution(nums):
    answer = 0
    for a in combinations(nums, 3): # 3중 for문 -> 조합
        cand = sum(a)
        for j in range(2, cand):
            if cand % j==0:
                break
        else:
            answer += 1
    return answer



print(solution([1,2,3,4])) # 1
print(solution([1,2,7,6,4])) # 4