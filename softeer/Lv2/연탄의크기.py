import sys

n = int(input())
arr = list(map(int, input().split()))

arr.sort()
answer = -100

# for i in range(n):
#     cnt = 0
#     for j in range(n):
#         if arr[j]%arr[i]==0 : cnt +=1
#     answer = max(answer, cnt)

for i in range(2, max(arr)+1):
    cnt = 0
    for j in range(n):
        if arr[j]%i==0 : cnt +=1
    answer = max(answer, cnt)


print(answer)