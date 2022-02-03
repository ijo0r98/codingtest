# 브루트 포스(완전탐색) > 영화감독 숌

n = int(input())

answer, cnt = 1, 0
while True:
    
    if '666' in str(answer): # 816ms
    # if str(answer).find('666') != -1: # 1160ms
        cnt += 1
    if cnt == n:
        print(answer)
        break
        
    answer += 1
