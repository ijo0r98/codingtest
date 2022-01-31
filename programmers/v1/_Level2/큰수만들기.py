# 2021.12.29
# 코딩테스트 연습 > 탐욕법(Greedy) > 큰 수 만들기

from itertools import combinations

# 1
def solution(number, k):
    answer = []
    idx_c = list(combinations([i for i in range(len(number))], k))
    for idx in idx_c:
        tmp = ''
        for i in range(len(number)):
            if i not in idx:
                tmp += (number[i])
        answer.append(int(tmp))

    return str(max(answer))

# 2
def solution(number, k):
    answer = 0
    idx_c = list(combinations([i for i in range(len(number))], k))
    for idx in idx_c:
        tmp = ''
        for i in range(len(number)):
            if i not in idx:
                tmp += (number[i])
        answer = answer if answer > int(tmp) else int(tmp)

    return str(answer)

# 3
def solution(number, k):
    answer = []
    for num in number:
        if not answer:
            answer.append(num)
        else:
            if k > 0:
                while answer[-1] < num:
                    answer.pop()
                    k -= 1
                    if not answer or k <= 0:
                        break
            answer.append(num) 
    answer = answer[:-k] if k > 0 else answer
    return ''.join(answer)

# 4
def solution(number, k):
    stack = []
    for num in number:
        while stack and stack[-1] < num and k > 0:
            k -= 1
            stack.pop()
        stack.append(num)
    if k != 0:
        stack = stack[:-k]
    return ''.join(stack)
    
        
print(solution("1924", 2))
# print(solution("1231234", 3))
# print(solution("4177252841", 4))