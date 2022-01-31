# 코딩테스트 연습 > 월간 코드 챌린지 시즌2 > 음양 더하기

def solution(absolutes, signs):
    answer = 0
    for i in range(len(absolutes)):
        answer = answer + absolutes[i] if signs[i] else answer - absolutes[i]
    return answer



print(solution([4, 7, 12], [True, False, True])) # 9
