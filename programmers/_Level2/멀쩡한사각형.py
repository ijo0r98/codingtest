# 코딩테스트 연습 > Summer/Winter Coding(2019) > 멀쩡한 사각형

import math

def solution(w, h):
    total = w * h
    height, width = max(w, h), min(w, h)

    if height % width == 0:
        return total - h
    
    disable = math.ceil(height / width)
    return total - (disable * width)


def solution(w, h):
    total = w * h
    height, width = max(w, h), min(w, h)

    if height % width == 0:
        return total - height

    # 최소공배수 크기 사각형 안의 사용할 수 없는 사각형
    disable = height + width - math.gcd(height, width)

    return total - disable


def solution(w,h):
    gcd = math.gcd(w, h) 
    answer = w * h - (w + h - gcd)
    return answer



print(solution(8, 12)) # 80
print(solution(20, 20)) # 380
print(solution(3, 4)) # 6
print(solution(100000000, 999999999)) # 99999998800000002
