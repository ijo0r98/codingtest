# 연습문제 > 두 정수사이 합

def solution(a, b):
    y, x = min(a,b), max(a, b)
    return (x*(x+1)/2) - (y*(y+1)/2) + y
    

# 다른 사람 풀이
def solution(a, b):
    if a > b:
        a, b = b, a
    
    return sum(range(a, b+1))