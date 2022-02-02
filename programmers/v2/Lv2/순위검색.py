# 2021 KAKAO BLIND RECRUITMENT > 순위 검색


# 1 정확도 테스트는 통과했지만 효율성 테스트는 통과 못함
import collections

def solution(info, query):
    answer = []
    info_arr = []
    
    info_lan = collections.defaultdict(set)
    info_dept = collections.defaultdict(set)
    info_career = collections.defaultdict(set)
    info_food = collections.defaultdict(set)
    info_score = []
    
    for idx, i in enumerate(info):
        i = list(i.split(' '))
        info_lan[i[0]].add(idx)
        info_dept[i[1]].add(idx)
        info_career[i[2]].add(idx)
        info_food[i[3]].add(idx)
        info_score.append(i[4])

    for q in query:
        candidates = set()
        q = list(q.split('and'))
        
        # language
        if q[0].strip() == '-':
            candidates = set([i for i in range(len(info))])
        else:
            candidates = info_lan[q[0].strip()]
        # print(q[0], info_lan[q[0].strip()], candidates)

        # dept
        if q[1].strip() != '-':
            candidates = candidates.intersection(info_dept[q[1].strip()])
        # print(q[1], info_dept[q[1].strip()], candidates)
        
        # career
        if q[2].strip() != '-':
            candidates = candidates.intersection(info_career[q[2].strip()])
        # print(q[2], info_career[q[2].strip()], candidates)
        
        # food
        tmp = list(q[3].split())
        if tmp[0] != '-':
            candidates = candidates.intersection(info_food[tmp[0]])
        # print(tmp[0], info_food[tmp[0]], candidates)
        
        cnt = 0
        for c in list(candidates):
            if int(info_score[c]) >= int(tmp[1]):
                cnt += 1
                
        answer.append(cnt)
        
    return answer