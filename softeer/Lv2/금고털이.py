import sys
input = sys.stdin.readline

w, n = map(int, input().split())
answer = 0



# v1.0
# prices={}
# for i in range(n):
#     inputs = list(map(int, input().split()))
#     prices[inputs[1]]=inputs[0] # key 가격 : value 무게
# for key in prices.keys(): 
#     if prices[key] <= w:
#         answer += (key * prices[key])
#         w -= prices[key]
#     else: 
#         answer += (w * key)
#         break


## v2.0
values = [list(map(int, input().split())) for _ in range(n)] # n만큼 리스트 저장하여 2차원 배열 생성 [m, p]
values = sorted(values, key=lambda x: x[1], reverse=True) # p값 기준 정렬 

for m, p in values:
    if m <= w:
        answer += (p*m)
        w -= m
    else :
        answer += (w*p)
        break   
    
print(answer)

# 1차 시도 실패 > 가격 기준으로 딕셔너리 생성, 같은 p일때 같은 m 겹쳐서 사라짐
# 2차 수정 > 딕셔너리가 아닌 이중배열로 인풋 저장
# https://softeer.ai/connect/devtalk/1357


    
