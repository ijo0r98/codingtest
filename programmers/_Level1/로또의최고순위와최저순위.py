# 코딩테스트 연습 > 2021 Dev-Matching: 웹 백엔드 개발자(상반기) > 로또의 최고 순위와 최저 순위

# 내 풀이
def solution(lottos, win_nums):
    answer = []
    get_result = {6: 1, 5: 2, 4: 3, 3: 4, 2: 5, 1: 6, 0: 6}  # 맞은 개수에 따른 순위

    cnt = lottos.count(0) # 0의 수
    correct = len(list(set(lottos) & set(win_nums))) # 일치한 숫자의 수 

    answer.append(get_result[correct + cnt])
    answer.append(get_result[correct])
    
    return answer


print('answer: ', solution([44, 1, 0, 0, 31, 25], [31, 10, 45, 1, 6, 19])) # [3, 5]
