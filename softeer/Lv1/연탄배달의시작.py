import sys

n = int(input())

dis = []
# points = list(input().split(" ")
points = list(map(int, input().split()))

for i in range(1, len(points)):
    dis.append(int(points[i])-int(points[i-1]))
    
min_dis = min(dis)
print(dis.count(min_dis))
