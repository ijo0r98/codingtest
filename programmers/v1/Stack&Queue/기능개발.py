# 고득점 kit > stack&queue > 기능개발(L2)

# Queue FIFO

# 1
def solution(progresses, speeds):
    answer = []

    time = 0
    count = 0
    
    while(len(progresses) > 0):
        if progresses[0] + time * speeds[0] >= 100:
            # FIFO - 앞의 기능이 배포될 때 뒤의 기능 배포
            progresses.pop(0)
            speeds.pop(0)
            count += 1
        
        else:
            if count > 0:
                answer.append(count)
                count = 0
            time += 1

    answer.append(count)
            
    return answer


# 2
def solution(progresses, speeds):
    Q = []
    for p, s in zip(progresses, speeds):
        if len(Q) == 0 or Q[-1][0] < -((p-100) // s):
            # 첫번째 반복문을 돌 때, -와 //로 올림연산
            Q.append([-((p-100) // s), 1]) # [첫번째 기능 개발에 필요한 날짜, 1]
        else:
            Q[-1][1] += 1 # count, 앞의 기능 개발 날짜 안에 포함되면 배포될 기능 수 ++
    return [q[1] for q in Q]


#####
p1, s1 = [93, 30, 55], [1, 30, 5]
print(solution(p1, s1)) # [2, 1]
# 2 실행모습
# [[7, 1]]
# [[7, 2], [9, 1]]

p2, s2 = [95, 90, 99, 99, 80, 99], [1, 1, 1, 1, 1, 1]
print(solution(p2, s2)) # [1, 3, 2]
# 2 실행모습
# [[5, 1]]
# [[5, 1], [10, 1]]
# [[5, 1], [10, 3], [20, 1]]
