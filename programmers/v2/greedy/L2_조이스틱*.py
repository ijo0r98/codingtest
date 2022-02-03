# 탐욕법 > 조이스틱

# 1
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

# 2
def solution(name):
    answer = 0
    max_dist, dist = 0, 0
    max_i, max_j = 0, 0
    last = 0
    for i, n in enumerate(name):
        if n != 'A':
            answer += min(abs(ord(n) - ord('A')), abs(ord('Z')-ord(n)+1))
            dist = 0 # A 거리 초기화해줌
            last = i
        else:
            dist += 1
            if max_dist < dist:
                max_dist = dist
                max_i, max_j = i-max_dist+1, i
                
    print(max_i, max_j, len(name), last)
    if max_dist == len(name):
        answer = 0
    elif max_dist != 0:
        tmp = min(((max_i-1)*2 + (len(name)-1-last)+1), ((len(name)-1-last)*2+1+(max_i-1)))
        answer += min(last, tmp)
    elif max_dist == 0:
        answer += last
    
    return answer

# 3
def solution(name):
    answer = 0
    max_dist, dist = 0, 0
    max_i, max_j = 0, 0
    last = 0
    for i, n in enumerate(name):
        if n != 'A':
            answer += min(abs(ord(n) - ord('A')), abs(ord('Z')-ord(n)+1))
            dist = 0 # A 거리 초기화해줌
            last = i
        else:
            dist += 1
            if max_dist < dist:
                max_dist = dist
                max_i, max_j = i-max_dist+1, i
                
    print(max_i, max_j, len(name), last)
    if max_dist == len(name):
        answer = 0
    elif max_dist != 0:
        print(((max_i)*2 + (len(name)-1-last)+1), ((len(name)-1-last)*2+1+(max_i)))
        tmp = min(((max_i)*2 + (len(name)-1-last)+1), ((len(name)-1-last)*2+1+(max_i-1)))
        answer += min(last, tmp)
    elif max_dist == 0:
        answer += last
    
    return answer


# 다른 사람 풀이
def solution_other(name):
    answer = 0
    min_left_right = len(name) # 왼쪽에서 오른쪽으로만 이동할 때 좌,우 조작 횟수
    next_idx = 0
    for idx, char in enumerate(name):
        # up/down
        answer += min(ord(char) - ord('A'), ord('Z') - ord(char) + 1)
        
        # left/right
        next_idx = idx + 1
        while next_idx < len(name) and name[next_idx] == 'A':
            next_idx += 1 # 현재 위치 이후 연속된 A 다음의 문자를 가리킴
        
        # 한 방향으로만 이동하는 경우와, 오른쪽으로 이동했다가 왼쪽으로 이동하는 경우를 비교
        min_left_right = min(min_left_right, idx + idx + len(name) - next_idx)
    answer += min_left_right
    return answer


# print(solution("BBBAAAB")) #8
# print(solution("ABABAAAAABA")) #10
# print(solution("ABABAAAAAB")) #8
# print(solution("BABAAAAB")) #7
# print(solution("BBBBAAAAAB")) #10
# print(solution("BBBBAAAABA")) #12

# print(solution("CANAAAAANAN")) #48
# print(solution("ABAAAAABAB")) #8
print(solution("AAB")) #2

## https://programmers.co.kr/questions/15137
# print(solution("BBBAAAB")) #8
# print(solution("ABABAAAAABA")) #10
# print(solution("CANAAAAANAN")) #48
# print(solution("ABAAAAABAB")) #8
# print(solution("ABABAAAAAB")) #8
# print(solution("BABAAAAB")) #7
# print(solution("AAA")) #0
# print(solution("ABAAAAAAABA")) #6
# print(solution("AAB")) #2
# print(solution("AABAAAAAAABBB")) #11
# print(solution("ZZZ")) #5
# print(solution("BBBBAAAAAB")) #10
# print(solution("BBBBAAAABA")) #12