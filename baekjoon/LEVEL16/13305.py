# 그리디 알고리즘 > 주유소

## 1 최소 기름값이 아닐 경우는 필요한만큼만 충전, 최소일 경우 모든 길이만큼 충전
# import sys
# n = int(sys.stdin.readline())
# roads = list(map(int, sys.stdin.readline().split()))
# prices = list(map(int, sys.stdin.readline().split()))
# min_price = min(prices[:-1])
# answer = 0
# for i in range(n): # 마지막 주유소는 필요없음
#     if prices[i] > min_price:
#         answer += (prices[i]*roads[i])
#     else:
#         answer += (prices[i]*sum(roads[i:]))
#         break
# print(answer)
## 최소값을 만나기 전, 더 적은 비용으로 충전할 수 있음 예) 5, 3, 4, 3, 2, .. 일 경우 2 이전에 3+4+3 보다 3으로 모두 주유하는게 더 쌈

# 2
# import sys
# n = int(sys.stdin.readline())
# roads = list(map(int, sys.stdin.readline().split()))
# prices = list(map(int, sys.stdin.readline().split()))
# answer = roads[0] * prices[0] # 첫 주유소에서는 무조건 주유해야함
# for i, price in enumerate(prices[1:]):
#     if price > prices[i-1]:
#         answer -= (prices[i-1] * roads[i-1]) # 이전에 더한 값 뺌
#         answer += price * 
#     else:
#         answer += (price * roads[i])

## 3 다른 사람 코드 참고
import sys
n = int(sys.stdin.readline())
roads = list(map(int, sys.stdin.readline().split()))
prices = list(map(int, sys.stdin.readline().split()))
answer = 0
min_price = prices[0]
for i in range(n-1):
    if min_price > prices[i]:
        min_price = prices[i]
    answer += min_price * roads[i]
print(answer)