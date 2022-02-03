# 완전탐색 > 카펫

# 1
def solution(brown, yellow):
    h = 3
    while True:
        w = int((brown+4-2*h)/2)
        Y = (w-2) * (h-2)
        if (Y==yellow):
            return [max(w, h), min(h, w)]
        h += 1
        
# 2 이차방정식 -> 근의 공식 이용한 풀이
import math
def solution(brown, yellow):
    w = ((brown+4)/2 + math.sqrt(((brown+4)/2)**2-4*(brown+yellow)))/2
    h = ((brown+4)/2 - math.sqrt(((brown+4)/2)**2-4*(brown+yellow)))/2
    return [w,h]
        
    