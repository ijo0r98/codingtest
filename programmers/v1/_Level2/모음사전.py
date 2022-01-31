# 코딩테스트 연습 > 위클리 챌린지 > 모음 사전

from collections import deque

def solution(word):
    vowels = ['A', 'E', 'I', 'O', 'U']
    answer = 0
    word = deque(list(word))
    length = len(word)
    
    while word:
        current = word.popleft()
        for i in range(5, vowels.index(current), -1):
            for j in range(5, length, -1):
                answer *= 5 ** vowels.index(current)

    return answer


# print(solution("AAAAE")) # 6
# print(solution("AAAE")) # 10
print(solution("I")) # 1563
# length=1, index('I') 2 
# len(vowels) = 5
