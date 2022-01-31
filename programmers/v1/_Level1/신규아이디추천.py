# 코딩테스트 연습 > 2021 KAKAO BLIND RECRUITMENT > 신규 아이디 추천

# 내 풀이
def solution(new_id):
    answer = ''

    # 1. 소문자로 모두 치환
    answer = new_id.lower() 

    # 2. 알파벳 소문자, 숫자, 빼기(-), 밑줄(_), 마침표(.)를 제외한 모든 문자를 제거
    for s in list(answer):
        if (s.isalpha() == True) | ('_' == s) | ('-' == s) | ('.' == s) | (s.isdigit() == True): 
            continue
        else:
            answer = answer.replace(s, "")
    
    # 3. 마침표(.)가 2번 이상 연속된 부분 하나의 마침표(.)로 치환
    answer = list(answer)
    i = 0
    while True:
        try:
            if i == len(answer) - 1:
                break
            if (answer[i] == '.') & (answer[i+1] == '.'):
                answer.pop(i)
                # i -= 1
            else:
                i += 1
        except:
            print(i)

    # 4. 마침표(.)가 처음이나 끝에 위치한다면 제거
    answer = ''.join(answer)
    if answer.startswith('.'):
        answer = answer[1:]
    if answer.endswith('.'):
        answer = answer[:-1]

    # 5. 빈 문자열이라면  "a" 대입
    if len(answer) == 0:
        answer += 'a'

    # 6. 길이가 16자 이상이면, 첫 15개의 문자를 제외한 나머지 문자들 모두 제거, 만약 제거 후 .가 끝에 위치한다면 . 제거
    if len(answer) >= 16:
        answer = answer[:15]
        if answer.endswith('.'):
            answer = answer[:-1]

    # 7. 길이가 2자 이하라면, 마지막 문자를 new_id의 길이가 3이 될 때까지 반복해서 끝에 연결
    if len(answer) <= 2:
        char = answer[-1:]
        while True:
            if len(answer) > 2:
                break
            answer += char
            
    return answer


# 다른 사람 풀이 1 (정규식 사용)
import re

def solution(new_id):
    st = new_id
    st = st.lower()
    st = re.sub('[^a-z0-9\-_.]', '', st)
    st = re.sub('\.+', '.', st)
    st = re.sub('^[.]|[.]$', '', st)
    st = 'a' if len(st) == 0 else st[:15]
    st = re.sub('^[.]|[.]$', '', st)
    st = st if len(st) > 2 else st + "".join([st[-1] for i in range(3-len(st))])
    return st


# 다른 사람 풀이 2
def solution(new_id):
    answer = ''
    # 1
    new_id = new_id.lower()
    # 2
    for c in new_id:
        if c.isalpha() or c.isdigit() or c in ['-', '_', '.']:
            answer += c
    # 3
    while '..' in answer:
        answer = answer.replace('..', '.')
    # 4
    if answer[0] == '.':
        answer = answer[1:] if len(answer) > 1 else '.'
    if answer[-1] == '.':
        answer = answer[:-1]
    # 5
    if answer == '':
        answer = 'a'
    # 6
    if len(answer) > 15:
        answer = answer[:15]
        if answer[-1] == '.':
            answer = answer[:-1]
    # 7
    while len(answer) < 3:
        answer += answer[-1]
    return answer


print('answer: ', solution("...!@BaT#*..y.abcdefghijklm..")) # "bat.y.abcdefghi"
print('answer: ', solution("z-+.^.")) # "z--"
print('answer: ', solution("123_.def")) # 123_.def
print('answer: ', solution("=.=")) # "aaa"
print('answer: ', solution('.......................')) # "aaa"
