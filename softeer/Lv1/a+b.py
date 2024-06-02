import sys

n = int(input())

for i in range(n):
    inputs = list(map(int, input().split(" ")))
    print("Case #"+str(i+1)+": "+str(inputs[0]+inputs[1]))