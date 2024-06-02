import sys
sys.setrecursionlimit(5000)

inputs = input()
n, m = int(inputs.split(" ")[0]), int(inputs.split(" ")[1])

arr = [[]]

for i in range(n):
    for j in range(n):
        arr[i][j]=int(input())