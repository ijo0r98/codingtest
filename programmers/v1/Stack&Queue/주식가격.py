# 고득점 kit > stack&queue > 주식가격(L2)

# prices 초단위 주식 가격 -> answer 각 가격별 마지막 가격 기준 가격이 떨어지지 않은 기간들(초)

# 1
def solution(prices):
    answer = []
    time = 0
    length = len(prices)

    for i in range(length):
        time = 0
        for j in range(i+1, length):
            if prices[i] > prices[j]:
                break
        answer.append(j-i)
        
    return answer


# 2
from collections import deque

def solution(prices):
    answer = []
    prices = deque(prices)
    while prices:
        c = prices.popleft()

        count = 0
        for i in prices:
            if c > i:
                count += 1
                break
            count += 1

        answer.append(count)

    return answer



#####
prices = [1, 2, 3, 2, 3]
print(solution(prices)) # [4, 3, 1, 1, 0]

prices = [5, 8, 6, 2, 4, 1]
print(solution(prices)) # [3, 1, 1, 2, 1, 0]