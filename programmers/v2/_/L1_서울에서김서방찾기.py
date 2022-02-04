# 연습문제 > 서울에서 김서방 찾기

def solution(seoul):
    for i, s in enumerate(seoul):
        if "Kim" in s:
            return "김서방은 {}에 있다".format(i)
        
def solution(seoul):
    return "김서방은 {}에 있다".format(seoul.index("Kim"))   