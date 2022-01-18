# 2675. 문자열 반복

n = int(input())

for i in range(n):
    cnt, S = map(str, input().split())
    new_S = ''
    for s in S:
        new_S += int(cnt) * s
    print(new_S)