# 스택/큐 > 기능개발

from math import ceil

def solution(progresses, speeds):
    answer = []
    days = []
    for i in range(len(progresses)):
        days.append(ceil((100-progresses[i])/speeds[i]))
    
    cnt = 1
    deploy = days[0]
    for day in days[1:]:
        if day <= deploy:
            cnt += 1
        else:
            answer.append(cnt)
            cnt = 1
            deploy = day
            
    answer.append(cnt)
        
    return answer