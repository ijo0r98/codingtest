# 연습문제 > 문자열 다루기 기본

def solution(s):
    if (len(s) == 4) or (len(s)==6):
        try:
            int_s = int(s)
            return True
        except:
            pass
        
    return False


# 다른 사람 풀이
def alpha_string46(s):
    return s.isdigit() and len(s) in (4, 6)
