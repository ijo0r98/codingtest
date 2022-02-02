# 완전탐색 > 소수 찾기

import itertools, math

def solution(numbers):
    answer = 0
    numbers = [str(n) for n in numbers]
    nums = set()
    
    for i in range(1, len(numbers)+1):
        for p in set(itertools.permutations(numbers, i)):
            num = int(''.join(p))
            if num > 1:
                nums.add(num)
    
    for num in nums:
        ck = True
        for i in range(2, int(math.sqrt(num))+1):
            if num % i == 0:
                ck = False
                break
        if ck:
            answer += 1
        
    return answer

