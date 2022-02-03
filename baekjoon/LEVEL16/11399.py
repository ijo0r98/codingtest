# 그리디 알고리즘 > ATM

import sys
n = int(sys.stdin.readline())
nums = list(map(int, sys.stdin.readline().split()))
times = []

for i, num in enumerate(nums):
    times.append((i, num))
times.sort(key=lambda x:x[1])

answer = 0
for i in range(1, len(times)+1):
    nums = list(map(lambda x: x[1], times[:i]))
    answer += sum(nums)

print(answer)