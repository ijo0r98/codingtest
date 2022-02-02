# 2021 KAKAO BLIND RECRUITMENT > 신규 아이디 추천

def solution(new_id):
    answer = []

    # 1
    new_id = new_id.lower()
    
    # 2
    for l in list(new_id):
        if (l.isalpha() == True) or (l.isdigit() == True) or (l in ['-', '_', '.']):
            answer.append(l)
            
    # 3
    cnt = 0
    for i in range(len(answer)):
        if answer[i] == '.':
            cnt += 1
            if cnt > 1:
                answer[i] = '*'
        else:
            cnt = 0
    answer = ''.join(answer).replace('*', '')
    
    # 4
    try:
        if answer[0] == '.':
            answer = answer[1:]
        if answer[-1] == '.':
            answer = answer[:-1]
    except:
        pass
    
    # 5
    if len(answer) == 0:
        answer += 'a'
    
    # 6
    if len(answer) >= 16:
        answer = answer[:15]
    if answer[-1] == '.':
        answer = answer[:-1]
    
    # 7
    last = answer[-1]
    if len(answer) <= 2:
        for i in range(3-len(answer)):
            answer += last
    
            
    return answer
