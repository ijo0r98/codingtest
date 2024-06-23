import sys
input = sys.stdin.readline

k, p, n = map(int, input().split())

# v=k
# for _ in range(n):
#     v *= p

# print(v%1000000007)

ans = k
for _ in range(n):
    ans = (ans*p)%1000000007

print(ans)

# v1.0 시간초과
# https://softeer.ai/connect/devtalk/1465