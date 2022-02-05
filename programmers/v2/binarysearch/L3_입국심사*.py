# 이분탐색 > 입국심사

# 다른 사람 풀이
def solution(n, times):
    answer = 0
    
    # right는 가장 비효율적으로 심사했을 때 걸리는 시간
    # 가장 긴 심사시간이 소요되는 심사관에게 n 명 모두 심사받는 경우이다.
    left, right = 1, max(times) * n
    while left <= right:
        mid = (left+ right) // 2
        people = 0
        for time in times:
            # people 은 모든 심사관들이 mid분 동안 심사한 사람의 수
            people += mid // time
            # 모든 심사관을 거치지 않아도 mid분 동안 n명 이상의 심사를 할 수 있다면 반복문을 나간다.
            if people >= n:
                break
        
        # 심사한 사람의 수가 심사 받아야할 사람의 수(n)보다 많거나 같은 경우
        if people >= n:
            answer = mid
            right = mid - 1
        # 심사한 사람의 수가 심사 받아야할 사람의 수(n)보다 적은 경우
        elif people < n:
            left = mid + 1
            
    return answer


# 내 풀이
def solution(n, times):
    answer = 0
    min_time, max_time = 1, max(times)*n
    
    while min_time <= max_time:
        mid = (min_time+max_time)//2 # 이분 탐색으로 최대와 최소의 중간값을 기준으로 판단
        people = 0 # 심사받는 사람
        for time in times:
            people += mid//time # 소요시간/심사시간 -> 해당 시간동안 심사 가능한 사람 수
            if people >= n: # 모두 검사가 완료되었으면 멈춤
                break
        if people >= n: # 모두 검사가 완료되었을 때
                answer = mid
                max_time = mid-1# 심사한 수가 더 많은 경우 min~mid로 범위 변경
                # 최소로 하기 위해 while 조건 min_time<=max_time을 위배하기 전까지 계속 범위를 줄임
                
        else: # 심사한 사람 수가 더 적은경우 시간을 늘려야함(범위를 mid~max로 변경)
            min_time = mid+1
    return answer
                
        
        
    