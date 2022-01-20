# 0120

# 겹치는 원의 쌍

# 1
def solution(A):
    answer = 0
    points = []
    for i in range(len(A)):
        points.append((i-A[i], -1)) # left
        points.append((i+A[i], 1)) # right
    points.sort() 
    print(points)   
    
    # (이전까지 -1의 개수) - 1(자기 자신)
    cnt_left = 0 # -1
    for i in range(len(points)):
        if points[i][1] == -1:
            cnt_left += 1
        if points[i][1] == 1:
            answer += (cnt_left-1)
    
    return -1 if answer > 10000000 else answer

# 2 100%
def solution(A):
    answer = 0
    points = []
    for i in range(len(A)):
        points.append((i-A[i], -1)) # left
        points.append((i+A[i], 1)) # right
    points.sort() 
    
    cnt_left = 0 # -1
    for i in range(len(points)):
        if points[i][1] == -1:
            answer += cnt_left
            cnt_left += 1
        if points[i][1] == 1:
            cnt_left -= 1
    
    return -1 if answer > 10000000 else answer



print(solution([1, 5, 2, 1, 4, 0]))