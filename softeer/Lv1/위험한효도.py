import sys

dis = list(map(int, input().split()))
a, b, d = dis[0], dis[1], dis[2]

# a초간 뒤를 봄 (이동 가능), b초간 앞을 봄 (이동 불가)
# 터치 후 변경
# a초간 앞을 봄 (이동 불가), b초간 뒤를 봄 (이동 가능)

s = 0
dis = 0

# 첫번째
n1 = int(d/a)
if d/a==1 :  n2 = 0 
else :  n2 = n1

s = (n1*a) + (n2*b) + (d - n1*a) # a만큼 이동, b만큼 휴식, a 이동 후 남은 거리

# 터치 후 두번째
m1 = int(d/b)
if d/b == 1: m2 = 0
else : m2 = m1
s += (m1*b) + (m2*a) + (d - m1*b)

print(s)
