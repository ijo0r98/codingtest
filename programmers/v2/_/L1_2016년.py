# 연습문제 > 2016년

# 윤년 2월이 29일까지
def solution(a, b):
    
    weeks = ['FRI', 'SAT', 'SUN', 'MON', 'TUE', 'WED', 'THU']
    days = b
    for i in range(1, a):
        if i in [1, 3, 5, 7, 8, 10, 12]:
            days += 31 
        elif i in [4, 6, 9, 11]:
            days += 30 
        elif i == 2:
            days += 29
        print(i, days)
            
    return weeks[days%7-1]
    
    