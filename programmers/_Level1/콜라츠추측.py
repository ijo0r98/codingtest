# 코딩테스트 연습 > 연습문제 > 콜라츠 추측

def solution(num):
    answwer = 0
    while answwer < 500:
        if num == 1:
            return answwer
        
        num = int(num / 2) if num % 2 == 0 else num * 3 + 1
        answwer += 1

    if answwer == 500:
        return -1


print(solution(6)) # 8
print(solution(16)) # 4
print(solution(626331)) # -1