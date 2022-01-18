# 코딩테스트 연습 > 연습문제 > 정수 내림차순으로 배치하기

def solution(n):
    new_arr = [i for i in str(n)]
    new_arr.sort(reverse=True)
    answer = ''.join(new_arr)
    return int(answer)


print(solution(118372)) # 873211