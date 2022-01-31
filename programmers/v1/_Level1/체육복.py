# 코딩테스트 연습 > 탐욕법(Greedy) > 체육복

def solution(n, lost, reserve):

    lost_uniq = list(set(lost) - set(reserve))
    reserve_uniq = list(set(reserve) - set(lost))
    answer = n - len(lost_uniq)

    for i in range(len(lost_uniq)):
        m = lost_uniq[i] - 1
        p = lost_uniq[i] + 1

        if m in reserve_uniq:
            answer += 1
            reserve_uniq.pop(reserve_uniq.index(m))
        elif p in reserve_uniq:
            answer += 1
            reserve_uniq.pop(reserve_uniq.index(p))

    return answer


print('answer: ', solution(5, [2, 4], [1, 3, 5])) # 5
print('answer: ', solution(5, [2, 4], [3])) # 4
print('answer: ', solution(3, [3], [1])) # 2
print('answer: ', solution(5, [3, 5], [2, 4])) # 5
print('answer: ', solution(7, [2,3,4], [1,2,3,6])) # 6
print('answer: ', solution(5, [1, 2], [2, 3])) # 4