# 0114
# 1차 100%

import collections

def solution(A):
    a_dict = collections.defaultdict(list)
    
    for i in range(len(A)):
        a_dict[A[i]].append(i)
    
    # answer = []
    for key, value in a_dict.items():
        if len(value)%2 != 0:
            return key
    
    
print(solution([9, 3, 9, 3, 9, 7, 9])) 