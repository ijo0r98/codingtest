# DFS/BFS > 타겟넘버(L2)

# 1


# 2
import collections

def solution(numbers, target):
    answer = 0
    stack = collections.deque([(0, 0)]) # 방문한 노드 - 양방향 큐
    
    while stack:
        sum, idx = stack.popleft()

        if idx == len(numbers): # 1의 수(numbers의 길이)와 트리 높이가 같아질때까지 그래프 생성
            if sum == target:
                answer += 1
        else:
            # -1, 1 더한 그래프 생성
            number = numbers[idx]
            stack.append((sum + number, idx + 1))
            stack.append((sum - number, idx + 1))

    return answer


# 3
def solution(numbers, target):
    if not numbers and target == 0 :
        return 1
    elif not numbers:
        return 0
    else:
        return solution(numbers[1:], target-numbers[0]) + solution(numbers[1:], target+numbers[0])


# 4
def dfs(nums, i, n, t):
    answer = 0
    if i == len(nums):
        if n == t:
            return 1
        else:
            return 0
            
    answer += dfs(nums, i+1, n+nums[i], t)
    answer += dfs(nums, i+1, n-nums[i], t)
    return answer

def solution(numbers, target):
    answer = dfs(numbers, 0, 0, target)
    return answer



print('answer: ', solution([1, 1, 1, 1, 1], 3)) # 5