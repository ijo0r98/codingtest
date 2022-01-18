# 코딩테스트 연습 > 2017 팁스타운 > 예상 대진표

import math
def solution(n, a, b):
    answer = 0
    while True:
        if a == b:
            return answer
        
        answer += 1
        a = math.ceil(a/2)
        b = math.ceil(b/2)
        


print(solution(8, 4, 7)) # 3
print(solution(8, 5, 8)) # 2
print(solution(8, 1, 2)) # 1