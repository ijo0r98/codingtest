# 그리디 알고리즘 > 잃어버린 괄호

import sys
ex = sys.stdin.readline().strip()

## 1 완전탐색으로 풀려함
# ex_arr = []
# k = 0
# answer = 10000000
# oprs = []
# for i in range(len(ex)-1):
#     if (ex[i] == '-') or (ex[i] == '+'):
#         ex_arr.append(int(ex[k:i]))
#         ex_arr.append(ex[i])
#         k = i + 1
#         oprs.append(len(ex_arr)-1)
# ex_arr.append(int(ex[k:]))

# ex_copy = ex_arr.copy()
# for opr in oprs:
#     ex_arr = ex_copy.copy()
#     if ex_arr[opr] == '+':
#         ex_arr[opr-1] = ex_arr[opr-1] + ex_arr[opr+1]
#     else:
#         ex_arr[opr-1] = ex_arr[opr-1] - ex_arr[opr+1]
#     ex_arr = ex_arr[:opr] + ex_arr[opr+2:]
#     tmp = ex_arr[0]
#     # print(ex_arr)
#     for i in range(1, len(ex_arr)-1):
#         if ex_arr[i] == '+':
#             tmp += ex_arr[i+1]
#         elif ex_arr[i] == '-':
#             tmp -= ex_arr[i+1]
#         # print(tmp)
    
#     answer = min(answer, tmp)
    
# print(answer)


## 2 처음 마이너스가 나오기 전까지 모두 더함 -> 마이너스 이후 값들 또한 모두 더해서 앞의 합에서 뺌
# 값이 최소가 되어야함으로 앞의 합이 가장 작아야함, 따라서 처음 나오는 마이너스를 기준으로 계산
ex = list(ex.split('-'))
answer = sum(map(int, ex[0].split('+'))) # 앞은 모두 +로 연결되어있음으로 더해줌
for e in ex[1:]:
    answer -= sum(map(int, e.split('+')))
print(answer)