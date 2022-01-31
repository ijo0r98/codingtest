# 코딩테스트 연습 > 2020 KAKAO BLIND RECRUITMENT > 괄호 변환

def solution(p):
    p = list(p) # array
    answer = p.copy() # str
    stack = []
    
    for i in range(len(p)):
        if not stack:
            if p[i] != '(': # 시작하는 괄호가 아닐 때
                answer[i] = toOther(p[i])
            stack.append(p[i])
        else:
            if p[i] != stack[-1]: # 스택의 맨 위 괄호와 매칭될 때 괄호쌍 완성
                stack.pop()
                if p[i] != ')': # 닫히는 괄호가 아닐 때
                    answer[i] = toOther(p[i])
            else:
                stack.append(p[i])
                answer[i] = '('
        # print(i, stack, ''.join(answer))
    return ''.join(answer)


def toOther(p):
    if p == '(':
        return ')'
    else:
        return '('
    
    

print(solution('(()())()')) # (()())()
print(solution(')(')) # ()
print(solution("()))((()")) # "()(())()"
print(solution(")()(")) # ()()