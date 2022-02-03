# 탐욕법 > 구명보트

# 1 보트 인원제한 2명인걸 못봄
def solution(people, limit):
    answer = 0
    people.sort(reverse=True)
    total = people.pop()
    while people:
        # print(answer, total, people)
        if total + people[-1] > limit:
            answer += 1
            total = 0
        else:
            total += people[-1]
            people.pop()

    return answer+1

# 2 최대 인원 2명 조건은 포함하였으나 최소 횟수 조건은 만족하지 못함
# 최소 조건을 만족하기 위해서는 큰 사람 먼저 태워서 보내야함
def solution(people, limit):
    answer = 0
    people.sort(reverse=True)
    
    while people:
        if len(people) < 2:
            answer += 1
            break
            
        if people[-2] + people[-1] <= limit:
            people.pop()
            people.pop()
        else:
            people.pop()
        answer += 1
        
    return answer


# 3
import collections
def solution(people, limit):
    answer = 0
    people.sort(reverse=True)
    people = collections.deque(people)
    
    while people:
        if len(people) < 2:
            answer += 1
            break
        if people[0] + people[-1] <= limit:
            people.pop()
            people.popleft()
        else:
            people.popleft()
        answer += 1
        
    return answer