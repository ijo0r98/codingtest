# 2020 KAKAO BLIND RECRUITMENT > 문자열 압축

def solution(s):
    N = len(s)
    answer = []
    
    for i in range(1, N+1): 
        tmp = s[0:i]
        cnt = 1
        new_s = ''
            
        for j in range(i, N+1, i):
            tmp2 = s[j:j+i]
            
            if tmp == tmp2:
                cnt += 1
                    
            else:
                new_s = new_s + str(cnt) + tmp if cnt > 1 else new_s + tmp    
                tmp = tmp2
                cnt = 1
                
            if (len(tmp2) < i) or (j+i) == N:
                new_s = new_s + str(cnt) + tmp if cnt > 1 else new_s + tmp    
                answer.append(len(new_s))
        
    return min(answer)