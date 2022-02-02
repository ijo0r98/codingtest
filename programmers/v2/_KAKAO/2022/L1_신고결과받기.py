# 2022 KAKAO BLIND RECRUITMENT > 신고 결과 받기

# 내 풀이 1
import collections

def solution(id_list, report, k):
    length = len(id_list)
    answer = [0] * length
    report = set(report)
    
    reported_cnt = collections.defaultdict(int) # 신고당한 사람
    id_dict = collections.defaultdict(list) # 신고 목록
    
    for r in report:
        ids = list(r.split(' '))
        reported_cnt[ids[1]] += 1
        id_dict[ids[0]].append(ids[1])
            
    for i in range(length):
        try:
            for id in id_dict[id_list[i]]:
                if reported_cnt[id] >= k:
                    answer[i] += 1
        except:
            pass
        
    return answer


# 다른 사람 풀이
def solution(id_list, report, k):
    answer = [0] * len(id_list)    
    reports = {x : 0 for x in id_list}

    for r in set(report):
        reports[r.split()[1]] += 1

    for r in set(report):
        if reports[r.split()[1]] >= k:
            answer[id_list.index(r.split()[0])] += 1

    return answer