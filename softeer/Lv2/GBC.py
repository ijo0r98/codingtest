import sys

n,m=map(int, input().split())
n_list=[list(map(int, input().split())) for _ in range(n)]
m_list=[list(map(int, input().split())) for _ in range(n)]

total = 100
for i in range(m):
    while m_list[i][0] <= 0:
        