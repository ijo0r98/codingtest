# 연습문제 > 가운데 글자 가져오기

from math import floor

# 1
def solution(s):
    n = len(s)
    idx = int(floor(n/2))
    if n%2 != 0:
        return s[idx]
    else:
        return s[idx-1:idx+1]
    

# 2
def solution(s):
    idx = int(floor(len(s)/2))
    return s[idx] if len(s)%2 != 0 else s[idx-1:idx+1]


# 다른 사람 풀이 1
def solution(s):
    return str[(len(s)-1)//2:len(s)//2+1]

# 다른 사람 풀이 2
def solution(str):
    a = len(str)
    if a % 2 == 0 :
        a = (a-2) / 2
    else :
        a = (a-1) / 2
    return str[int(a) : -int(a)]