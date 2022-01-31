# 고득점 kit > hash > 위장(L2)

# 1
def solution(clothes):
    answer = 1
    clothes_dict = {}
    clothes_list = []

    for c in clothes:
        clothes_dict[c[1]] = 0
        clothes_list.append(c[1])

    for c in clothes:
        clothes_dict[c[1]] += 1
        
    clothes_list = list(set(clothes_list))

    for i in range(len(clothes_list)):
        answer *= (clothes_dict[clothes_list[i]] + 1)
        
    return answer - 1


# 2
def solution(clothes):
    clothes_type = {}

    for _, t in clothes:
        if t not in clothes_type:
            clothes_type[t] = 2
        else:
            clothes_type[t] += 1

    answer = 1
    for num in clothes_type.values():
        answer *= answer

    return answer - 1


# 3
from collections import Counter
from functools import reduce

def solution(clothes):
    cnt = Counter([kind for name, kind in clothes])
    answer = reduce(lambda x, y: x * (y + 1), cnt.values(), 1) - 1
    return answer



#####
# 예1) headgeer 2, eyewear 1 -> 3 * 2 -1
print(solution([["yellowhat", "headgear"], ["bluesunglasses", "eyewear"], ["green_turban", "headgear"]]))
# 예2) face 3 -> 4 * 1 - 1 = 3
print(solution([["crowmask", "face"], ["bluesunglasses", "face"], ["smoky_makeup", "face"]]))
# 예3) A 3, B 4, C 2 -> 4 * 5 * 3 - 1 = 59
temp = [['a1', 'A'], ['a2', 'A'], ['a3', 'A'], ['b1', 'B'], ['b2', 'B'], ['b3', 'B'], ['b4', 'B'], ['c1', 'C'], ['c2', 'C']]
print(solution(temp))