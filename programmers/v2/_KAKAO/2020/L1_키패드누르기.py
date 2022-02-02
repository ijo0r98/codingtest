# 2020 카카오 인턴십 > 키패드 누르기

# 1
from math import ceil

def solution(numbers, hand):
    answer = ''
    left = 10 # '*'
    right = 12 # '#'
    
    
    for num in numbers:
        if num == 0:
            num = 11
        if num in [1, 4, 7]:
            answer += 'L'
            left = num
        elif num in [3, 6, 9]:
            answer += 'R'
            right = num
        else:
            left_dist = abs(num-left)//3 if left%3 == 2 else abs(num-(left+1))//3 + 1
            right_dist = abs(num-right)//3 if right%3 == 2 else abs(num-(right-1))//3 + 1
            # print(num, ': left-', left, left_dist, ' right-', right, right_dist)
            
            if left_dist < right_dist:
                answer += 'L'
                left = num
            elif left_dist > right_dist:
                answer += 'R'
                right = num
            else:
                if hand == 'left':
                    answer += 'L'
                    left = num
                else:
                    answer += 'R'
                    right = num

    return answer