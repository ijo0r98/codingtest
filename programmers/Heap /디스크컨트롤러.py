# 고득점 kit > heap > 디스크 컨트롤러(L3)

# 작업 완료까지 평균 대기시간 최소가 되도록

# 1
def solution(jobs):
    answer = 0
    now = 0 # 현재 시점
    length = len(jobs)

    jobs = sorted(jobs, key=lambda x: x[1]) # 작업 소요시간 기준 정렬

    while len(jobs) != 0:
        for i in range(len(jobs)): # jobs의 수가 줄어들면서 i는 계속 0
            if jobs[i][0] <= now: # jobs의 가장 맨 앞의 작업이 완료되면
                now += jobs[i][1] # 현재 시간 + 해당 작업 소요시간
                answer += now - jobs[i][0] # 총 대기시간 += 현재 시점 - 작업이 들어온 시점
                jobs.pop(i) # 해당 작업 삭제
                break

            if i == len(jobs) - 1: # 작업이 아직 끝나지 않으면
                now += 1

    return answer // length


# 2
import heapq

def solution(jobs):
    count, last, answer = 0, -1, 0
    heap = []
    jobs.sort()
    time = jobs[0][0] # 현재 시점(첫번째로 들어온 작업은 가장 먼저 수행)
    
    while count < len(jobs):
        for s, t in jobs:
            if last < s <= time: # 작업 소요시간 기준 min heap, 계속해서 힙 감소
                heapq.heappush(heap, (t, s))
        
        if len(heap) > 0: # 바로 수행할 수 있는 작업이 있는 경우
            count += 1 
            last = time # 현재 시점
            term, start = heapq.heappop(heap) # 소요 시간, 들어온 시점
            time += term # 현재 시점 += 소요 시간
            answer += (time - start) # 총 대기시간 += 현재 시점(완료시간) - 들어온 시점
        else: # 바로 수행할 수 있는 작업이 없는 경우
            time += 1 
    return answer // len(jobs)


##### 
jobs = [[0, 3], [1, 9], [2, 6]]
print(solution(jobs)) # 9