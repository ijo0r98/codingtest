import sys

answer= 0 
for i in range(5):
    times = list(input().split(" "))
    t1 = list(times[0].split(":"))
    h1, m1 = int(t1[0]), int(t1[1])
    t2 = list(times[1].split(":"))
    h2, m2 = int(t2[0]), int(t2[1])
    
    if t2[1] < t1[1] :
        answer += (60-m1)+m2
        answer += (h2-h1-1)*60
    else :
        answer += (m2-m1)
        answer += (h2-h1)*60
        
print(answer)