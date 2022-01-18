# 코딩테스트 연습 > 연습문제 > 이상한 문자 만들기

# 짝수번째 알파벳은 대문자로, 홀수번째 알파벳은 소문자로

def solution(string):
    
    # string = string.split() # String[] split(String regex, int limit) 
    string = string.split(" ", -1)
    answer = ''
    
    for s in string:
        tmp = ''
        for i in range(len(s)):
            tmp += s[i].upper() if i % 2 == 0 else s[i].lower()
        answer += tmp + ' '

    return answer[:-1]

print(solution("try hello world")) # "TrY HeLlO WoRlD"
print(solution("AAAAAAAAAAA A A A A AAAAA AAA ") + '/')
print(solution("A ") + '/')