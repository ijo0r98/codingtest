# 1152. 단어의 개수

string = input()

def solution1(string):
    if string == ' ':
        return 0
    answer = 1
    for i in range(1, len(string)-1):
        if (string[i] == ' '):
            answer += 1
    return answer 

def solution2(string):
    return len(string.split())

print(solution2(string))
