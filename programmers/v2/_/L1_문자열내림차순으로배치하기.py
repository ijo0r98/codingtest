# 연습문제 > 문자열 내림차순으로 배치하기

def solution(s):
    s = list(s)
    s.sort(reverse=True)
    return ''.join(s)