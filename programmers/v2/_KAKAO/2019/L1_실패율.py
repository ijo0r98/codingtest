# 2019 KAKAO BLIND RECRUITMENT > 실패율

# 1
def solution(N, stages):
    answer = []
    
    stage_num = [i+1 for i in range(N+1)]
    stage_dict = dict.fromkeys(stage_num, 0)
    
    for stage in stages:
        stage_dict[stage] += 1
    
    total = len(stages)
    tmp = 0
    for key, itm in stage_dict.items():
        if key <= N:
            if total == 0:
                answer.append((key, 0))
            else:
                fail = itm/total
                total -= itm
                answer.append((key, fail))

    answer.sort(key=lambda x:x[1], reverse=True)
    
    
    return [x[0] for x in answer]