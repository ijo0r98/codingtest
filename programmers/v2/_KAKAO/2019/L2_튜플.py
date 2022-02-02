# 2019 카카오 개발자 겨울 인턴십 > 튜플

def solution(string):
    answer = []
    string = string.replace(',{','')
    sets = list(string[2:-2].split('}'))
    new_sets = []
    for s in sets:
        s = s.split(',')
        s = [int(x) for x in s]
        new_sets.append((s, len(s)))
    
    new_sets.sort(key=lambda x : x[1])
    
    answer.append(new_sets[0][0][0])
    for i in range(0, len(new_sets)-1):
        tmp_set = set(new_sets[i+1][0]) - set(new_sets[i][0])
        answer.append(list(tmp_set)[0])
    
    return answer


# 다른 사람 풀이 1
def solution(s):
    answer = []

    s1 = s.lstrip('{').rstrip('}').split('},{')

    new_s = []
    for i in s1:
        new_s.append(i.split(','))

    new_s.sort(key = len)

    for i in new_s:
        for j in range(len(i)):
            if int(i[j]) not in answer:
                answer.append(int(i[j]))

    return answer


# 다른 사람 풀이 2
from collections import Counter
def solution(s):
    new_s = [sss.replace('{','').replace('}','') for sss in s.split(',')]
    return [int(c[0]) for c in sorted(Counter(new_s).items(), key = lambda x: x[1],reverse=True )]