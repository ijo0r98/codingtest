# 코딩테스트 연습 > 찾아라 프로그래밍 마에스터 > 폰켓몬

def solution(nums):
    types = len(set(nums))
    d = int(len(nums) / 2)
    return types if types <= d else d

def solution(nums):
    return min(len(nums)/2, len(set(nums)))


print(solution([3,1,2,3])) # 2
print(solution([3,3,3,2,2,4])) # 3
print(solution([3,3,3,2,2,2])) # 2
