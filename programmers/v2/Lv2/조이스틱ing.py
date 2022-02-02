# 탐욕법 > 조이스틱

def solution(name):
    answer = 0
    
    max_dist, dist = 0, 0
    max_i, max_j = 0, 0
    last = 0
    for i, n in enumerate(name):
        if n != 'A':
            answer += min(abs(ord(n) - ord('A')), abs(ord('Z')-ord(n)+1))
            last = i
        else:
            dist += 1
            if max_dist < dist:
                max_dist = dist
                max_i, max_j = i-max_dist+1, i   

    if max_dist == len(name):
        answer = 0
    elif max_dist != 0:
        answer += min(last, ((max_i-1)*2 + (len(name)-max_j-2) + 1))
    elif max_dist == 0:
        answer += (last)
    
    return answer