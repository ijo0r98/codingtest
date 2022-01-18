# 코딩테스트 연습 > 연습문제 > JadenCase 문자열 만들기

# 첫 문자는 대문자, 나머지는 소문자

def solution(str):
    s_list = list(str)
    answer = s_list[0].upper()
    
    for i in range(1, len(s_list)):
        if s_list[i-1] == ' ':
            answer += s_list[i].upper()
        else:
            answer += s_list[i].lower()
    
    return answer


def Jaden_Case(s):
    # 내장함수 사용
    return s.title()


def Jaden_Case(s):
    # 공백 기준으로 단어 나눔(split()) -> 맨 앞글자는 대문자로, 나머지는 소문자로
    answer =[]
    for i in range(len(s.split())):
        answer.append(s.split()[i][0].upper() + s.split()[i].lower()[1:]) 
    return " ".join(answer)


print(Jaden_Case("3people unFollowed me")) # 3people Unfollowed Me

