import sys


# 대표적인 DFS 문제
# https://khw11044.github.io/study/codingtest/2023-04-13-cote12/
# https://jie0025.tistory.com/424

# dx, dy 인덱스 조합하여 상하좌우 탐색
dx=[-1,0,1,0] 
dy=[0,1,0,-1] 
    
def DFS(x, y):
    global cnt
    cnt += 1 
    arr[x][y]=0 # 탐색한 곳은 0으로 
    for i in range(4):
        # 상하좌우 탐색을 위해
        xx = x+dx[i] 
        yy = y+dy[i]
        if 0<=xx<n and 0<=yy<n and arr[xx][yy]==1 :
            DFS(xx, yy)
    
    
        

n=int(input())
arr = []
for i in range(n):
    inputs = list(map(int, input().split()))
    arr.append(inputs)
        
answer = []
for i in range(n):
    for j in range(n):          
        if arr[i][j]==1:      # 1이 발견되면 장애물
            cnt=0
            DFS(i,j)            # 1이 발견되면 해당 위치 기준으로 주변 탐색
            answer.append(cnt)     
    
print(len(answer))
for x in sorted(answer):
    print(x)  