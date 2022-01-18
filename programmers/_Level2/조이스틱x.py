# 코딩테스트 연습 > 탐욕법(Greedy) > 조이스틱

# 참고한 글  https://programmers.co.kr/questions/20983
# A 65 ~ Z 90 -> 26 

# 1 (정답률 60%)
def solution2(name):
    answer = 0
    length = len(name)
    
    i = 0
    ck = 0
    for i in range(length):
        if name[i] != 'A':
            diff = ord(name[i])-ord('A') if ord(name[i])-ord('A') < 13 else 26 - (ord(name[i])-ord('A'))
            answer += diff
            if ck < length - ck:
                answer += ck
            else:
                answer += (length-ck)
            ck = 1
        else:
            ck += 1

    return answer

# 2
def solution(name):
    answer = 0
    length = len(name)
    
    # up/down 
    for i in range(length):
        if name[i] != 'A':
            answer += min(ord(name[i])-ord('A'), ord('Z') - ord(name[i]) + 1)
            
    # left/right
    cnt = 0
    for i in range(length):
        # print(i, answer)
        if name[i] == 'A':
            cnt += 1
        if (name[i] != 'A') and (name[i-1] == 'A'):
            start = i - cnt - 1 if i - cnt - 1 >= 0 else 0
            end = i
            # print("{}: start {} / end {}".format(i, start, end))
            right = end - start
            left = start + length - end 
            answer += min(right, left)
            answer += start
            # print("{}: right {}, left {}, answer {}".format(i, right, left, answer))
        
    if cnt == 0: # 연속된 A가 아예 없을 때
        answer += length-1
         
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


# print(solution("JEROEN")) # 56
# print(solution("JAN")) # 23 (9 + 1 + 13)
# print(solution("JAAAN")) # 23 (9 + 13 + 1)
print(solution('ABABAAAAAAABA')) # 10
# print(solution('ZZAAAZZ')) # 8
# print(solution('AAAABABAAAA')) # 8