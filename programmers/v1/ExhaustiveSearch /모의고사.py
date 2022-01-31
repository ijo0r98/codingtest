# 완전탐색 > 모의고사(L1)

# 1
def solution(answers):
    answer = []
    n = len(answers)
    
    p1 = [1, 2, 3, 4, 5] # 5
    p2 = [2, 1, 2, 3, 2, 4, 2, 5] # 8
    p3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5] # 10
    
    a1, a2, a3 = 0, 0, 0
    
    for i in range(n):
        if answers[i] == p1[i % 5]: 
            a1 += 1
        if answers[i] == p2[i % 8]: 
            a2 += 1
        if answers[i] == p3[i % 10]: 
            a3 += 1

    answer.append((1, a1))
    answer.append((2, a2))
    answer.append((3, a3))
        
    # filter
    max_p = max(answer, key=lambda x: x[1])
    max_list = list(filter(lambda x: x[1] == max_p[1], answer))
    idx_list = list(map(lambda x: x[0], max_list))

    return idx_list


# 2 
def solution(answers):
    pattern1 = [1,2,3,4,5]
    pattern2 = [2,1,2,3,2,4,2,5]
    pattern3 = [3,3,1,1,2,2,4,4,5,5]
    score = [0, 0, 0]
    result = []

    for idx, answer in enumerate(answers):
        if answer == pattern1[idx%len(pattern1)]:
            score[0] += 1
        if answer == pattern2[idx%len(pattern2)]:
            score[1] += 1
        if answer == pattern3[idx%len(pattern3)]:
            score[2] += 1

    for idx, s in enumerate(score):
        if s == max(score):
            result.append(idx+1)

    return result


# 3
def solution(answers):
    p = [[1, 2, 3, 4, 5],
         [2, 1, 2, 3, 2, 4, 2, 5],
         [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]]
    s = [0] * len(p)

    for q, a in enumerate(answers):
        for i, v in enumerate(p):
            if a == v[q % len(v)]:
                s[i] += 1
    return [i + 1 for i, v in enumerate(s) if v == max(s)]



print('answer: ', solution([1, 2, 3, 4, 5])) # 1
print('answer: ', solution([1, 3, 2, 4, 2])) # 1, 2, 3