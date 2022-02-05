# 깊이/너비 우선 탐색(DFS/BFS) > 타겟 넘버

# 이전 재귀 코드 참고..

# 깊이우선탐색(DFS)
def solution(numbers, target):
    return dfs(numbers[0], numbers[1:], target) + dfs((-1) * numbers[0], numbers[1:], target)

def dfs(sum, nums, target):
    answer = 0
    try:
        if not nums:
            if sum == target:
                return 1
            else:
                return 0

        answer += dfs(sum + nums[0], nums[1:], target)
        answer += dfs(sum - nums[0], nums[1:], target)
        return answer
        
    except:
        print(sum, nums, target)
    


# 2 다시 풀어도 어려움..
def dfs(k, target, numbers):
    answer = 0
    try:
        if not numbers:
            if k == target:
                return 1
            else:
                return 0

        answer += dfs(k + numbers[0], target, numbers[1:])
        answer += dfs(k - numbers[0], target, numbers[1:])
        return answer
    
    except:
        print(answer, target, numbers)

def solution(numbers, target):
    return (dfs(numbers[0], target, numbers[1:])) + (dfs(numbers[0]*(-1), target, numbers[1:]))