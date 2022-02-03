# 브루트 포스(완전탐색) > 블랙잭

from itertools import combinations

answer = 0
n, m = map(int, input().split())
nums = list(map(int, input().split()))
orders = list(combinations(nums, 3))

for order in orders[::-1]:
    s = sum(order)
    if s <= m:
        answer = max(s, answer)
        
print(answer)
