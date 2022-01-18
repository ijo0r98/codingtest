# 1065. 한수

n = int(input())

def get_cnt(n):
    cnt = 99
    if n < 100: # 100 미만의 수는 모두 한수
        return n
    else:
        for i in range(100, n+1):
            if chk_han(i):
                cnt += 1
                
    return cnt

def chk_han(n):
    one = int(str(n)[2])
    ten = int(str(n)[1])
    hundred = int(str(n)[0])
    if (one-ten) == (ten-hundred):
        return True
    return False        

print(get_cnt(n))