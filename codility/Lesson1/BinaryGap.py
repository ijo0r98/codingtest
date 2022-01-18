# 0114
# 1차 66% -> 2차 4% -> 3차 100%

# def solution(N):
#     binary = bin(N)[2:]
#     i = 0
#     max_cnt = 0
#     for i in range(1, len(binary)-2):
#         if binary[i] == '0':
#             next_i = i + 1
#             cnt = 1
#             while True:
#                 cnt += 1
#                 next_i += 1
#                 if next_i == len(binary)-1:
#                     break
#                 if binary[next_i] == '1':
#                     max_cnt = max(cnt, max_cnt)
#                     break
                
#     return max_cnt

def solution(N):
    binary = bin(N)[2:]
    idxs = []
    for i in range(len(binary)):
        if binary[i] == '1':
            idxs.append(i)
    if len(idxs) == 1:
        return 0
    
    max_cnt = 0
    for i in range(len(idxs)-1):
        max_cnt = max(max_cnt, idxs[i+1]-idxs[i]-1)
    return max_cnt
            

print(solution(529)) # 4
print(solution(1041)) # 5
print(solution(32)) # 0
print(solution(1)) # 0
print(solution(100)) # 2