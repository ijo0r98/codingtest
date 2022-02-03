# 브루트 포스(완전탐색) > 덩치

n = int(input())
answer = [1 for i in range(n)]
info = []
for i in range(n):
    info.append(list(map(int, input().split())))

for i in range(n):
    for j in range(n):
        if (info[i][0] < info[j][0]) and (info[i][1] < info[j][1]):
            answer[i] += 1

for i in range(n):
    print(answer[i], end=' ')