import sys
from itertools import permutations, combinations

n = int(input())
arr = list(map(int, input().split(" ")))

# 조합
# arr_com  = list(combinations(arr, 2))
# arr_com_sq = []
# for i in range(len(arr_com)):
#     arr_com_sq.append(arr_com[i][0]*arr_com[i][1])
    
# print(max(arr_com_sq))

arr.sort()
answer = max(arr[0] * arr[1], arr[n-1] * arr[n-2])
print(answer)