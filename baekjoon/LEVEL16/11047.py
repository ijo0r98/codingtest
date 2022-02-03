# 그리디 알고리즘 > 동전 0

n, k = map(int, input().split())
coins = []
for i in range(n):
    coins.append(int(input()))

answer = 0
total = 0
for coin in coins[::-1]: # 최소 개수를 구해야하기 때문에 가장 단위가 큰 동전부터 고려하는 것이 탐욕법
    if (k - total) >= coin:
        answer = answer + (k-total)//coin
        total = total + (k-total)//coin * coin
    else:
        pass
    
    if total == k:
        print(answer)
        break