# 코딩테스트 연습 > 연습문제 > 직사각형 별찍기

n, m = map(int, input().strip().split(' '))
for i in range(m):
    for j in range(n):
        print('*', end="")
    print('')

for i in range(m):
    print('*' * n)