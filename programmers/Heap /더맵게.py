# 고득점 kit > heap > 더 맵게(L2)

# 섞은 음식의 스코빌 지수 = 가장 맵지 않은 음식의 스코빌 지수 + (두 번째로 맵지 않은 음식의 스코빌 지수 * 2)
# 모든 음식의 스코빌 지수가 k 이상이 되도록 반복
# 최소 몇번 섞어야 하는지 반환

# 1
import heapq

def solution(scoville, K):
    answer = 0
    
    while True:
        min1 = heapq.heappop(scoville)
        if (len(scoville) == 0) & (min1 < K):
            return -1
        elif min1 < K:
            answer += 1
            min2 = heapq.heappop(scoville)
            heapq.heappush(scoville, min1 + min2 * 2)
        else:
            return answer

# 1-2
def solution(scoville, K):
    answer = 0
    scovile = heapq.heapify(scoville)

    while len(scoville) != 1:    
        min1 = scoville[0]
        if min1 < K:
            answer += 1
            heapq.heappop(scoville)
            min2 = heapq.heappop(scoville)
            heapq.heappush(scoville, min1 + min2 * 2)
        else:
            return answer

    if scoville[0] > K:
        return answer
    return -1

# 1-3
def solution2(scoville, K):
    answer = 0
    scovile = heapq.heapify(scoville)

    while len(scoville) != 1:    
        min1 = scoville[0]
        if min1 < K:
            answer += 1
            heapq.heappop(scoville)
            min2 = heapq.heappop(scoville)
            heapq.heappush(scoville, min1 + min2 * 2)
        else:
            return answer

    if scoville[0] > K:
        return answer
    return -1


# 2
def solution(scoville, K):

    heapq.heapify(scoville)
    answer = 0
    while True:
        min = heapq.heappop(scoville)
        if min >= K:
            break
        if len(scoville) == 0:
            return -1
        min2 = heapq.heappop(scoville)
        heapq.heappush(scoville, min + min2 * 2)
        answer += 1  

    return answer


# 3
def solution(scoville, K):
    heapq.heapify(scoville)
    size, cnt = len(scoville) - 1, 0
    min = heapq.heappop(scoville)
    while size > 0:
        min = heapq.heappop(scoville)
        min2 = heapq.heappushpop(scoville, min + min2 + min2)
        if min >= K:
            return cnt + 1
        cnt += 1
        size -= 1
    return -1


s, k = [1, 2, 3, 9, 10, 12], 1
# s, k = [1, 2], 3
# s, k = [0, 0, 1], 3
# s, k = [0, 0, 0, 0, 3], 9
print(solution(s, k)) 