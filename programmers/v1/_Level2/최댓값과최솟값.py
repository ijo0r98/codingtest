# 코딩테스트 연습 > 연습문제 > 최댓값과 최솟값

def solution(s):
    nums = s.split(' ')
    nums = [int(num) for num in nums]
    answer = str(min(nums)) + ' ' + str(max(nums))
    return answer

def solution(s):
    s = list(map(int,s.split()))
    return str(min(s)) + " " + str(max(s))
    

print(solution("-1 -2 -3 -4")) # -4 -1
print(solution("1 2 3 4")) # 1 4