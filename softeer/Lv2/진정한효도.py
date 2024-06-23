import sys

arr = []
for i in range(3):
    arr.append(list(map(int, input().split())))

answer=100
for i in range(3):
    col = max(arr[i][0], arr[i][1], arr[i][2]) - min(arr[i][0], arr[i][1], arr[i][2])
    row = max(arr[0][i], arr[1][i], arr[2][i]) - min(arr[0][i], arr[1][i], arr[2][i])
    answer = min(answer,min(col, row))
    
print(answer)
    