# 2021 KAKAO BLIND RECRUITMENT > 메뉴 리뉴얼

from itertools import combinations
from collections import defaultdict

def solution(orders, counts):
    answer = []
    course_cnt = defaultdict(dict)
    
    for order in orders: 
        for c in counts:
            if c <= len(order):
                courses = list(combinations(list(order), c))
                for course in courses:
                    course_key = ''.join(sorted(course))
                    try:
                        course_cnt[c][course_key] += 1
                    except:
                        course_cnt[c][course_key] = 1

    
    for c, courses in course_cnt.items():
        max_c = max(courses.values()) if max(courses.values()) > 2 else 2
        for key, itm in courses.items():
            if max_c == itm:
                answer.append(key)
    
    return sorted(answer)
