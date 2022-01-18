# 코딩테스트 연습 > 연습문제 > 2016년

# 2016년 1월 1일은 금요일(FRI)
# 2016년은 윤년으로 2월이 29일까지 존재
# SUN, MON, TUE, WED, THU, FRI, SAT

def solution(a, b):
    # 요일
    answer = {
        0: 'FRI', 1: 'SAT', 2: 'SUN', 3: 'MON', 4: 'TUE', 5: 'WED', 6: 'THU'
    }
    # 전체 일수 계산
    if a in (3, 5, 7, 8, 10, 12):
        month = 31
    elif a == 1:
        month = 0
    elif a == 2:
        month = 29
    else:
        month = 30
    days = a * month + b
    return answer[days % 7]
    

print(solution(5, 24)) # "TUE"
print(solution(1, 3)) # "TUE"