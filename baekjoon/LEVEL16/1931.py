# 그리디 알고리즘 > 회의실 배정

n = int(input())
meetings = []
for i in range(n):
    meetings.append(list(map(int, input().split())))
    
meetings.sort(key=lambda x: (x[1], x[0])) # 더 많은 회의 진행을 위해 빨리 끝나는 회의 -> 빨리 시작하는 회의 순으로 정렬

answer = 1
end_time = meetings[0][1] # 첫번째 회의 끝나는 시간
for meeting in meetings[1:]:
    if end_time <= meeting[0]: # 앞의 회의 끝나는 시간이 다음 회의 시작하는 시간보다 작을 때 다음 회의 진행 가능
        answer += 1
        end_time = meeting[1]
        
print(answer)


# 다른 사람 풀이
# sys 라이브러리 이용해서 시간 단축하기
import sys

n = int(sys.stdin.readline())
meetings = []

for _ in range(n):
    meetings.append(list(map(int, sys.stdin.readline().split())))

meetings = sorted(meetings, key=lambda x: (x[1], x[0]))

answer = 1
end_time = meetings[0][1] 
for meeting in meetings[1:]:
    if end_time <= meeting[0]: 
        answer += 1
        end_time = meeting[1]
        
print(answer)
