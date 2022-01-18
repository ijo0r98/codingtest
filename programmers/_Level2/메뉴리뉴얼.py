# 코딩테스트 연습 > 2021 KAKAO BLIND RECRUITMENT > 메뉴 리뉴얼

from itertools import combinations
from collections import defaultdict

def solution(orders, course):
    answer = []
    menus = defaultdict(dict)
    
    for order in orders:
        for c in course:
            for menu in list(combinations(list(order), c)):
                menu = sorted(menu)
                menu = ''.join(menu)
                if menu not in menus[c].keys():
                    menus[c][menu] = 1
                else:
                    menus[c][menu] += 1
                    
    for c in course:
        if menus[c].values():
            maxcnt = max(menus[c].values())
        else: 
            continue
        if maxcnt >= 2:
            for key, value in menus[c].items():
                if value == maxcnt:
                    answer.append(key)
            
    return sorted(answer)


print(solution(["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"], [2,3,4])) # ["AC", "ACDE", "BCFG", "CDE"]
print(solution(["ABCDE", "AB", "CD", "ADE", "XYZ", "XYZ", "ACD"], [2,3,5])) # ["ACD", "AD", "ADE", "CD", "XYZ"]
print(solution(["XYZ", "XWY", "WXA"], [2, 3, 4])) # ["WX", "XY"]