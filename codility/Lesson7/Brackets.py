# 0129

# 괄호 확인 문제

# 1 -> 37%
def solution(S):
    tmp = []
    for s in S:
        if (s=='(') or (s=='[') or (s=='{'):
            tmp.append(s)
        elif s==')':
            if tmp[-1] != '(':
                return 0
            else: # ()
                tmp.pop()
        elif s==']':
            if tmp[-1] != '[':
                return 0
            else: # []
                tmp.pop()
        elif s=='}':
            if tmp[-1] != '{':
                return 0
            else: # {}
                tmp.pop()
    return 1

# 2 -> 100%
def solution(S):
    tmp = []
    for s in S:
        if (s=='(') or (s=='[') or (s=='{'):
            tmp.append(s)
        elif s==')':
            if (len(tmp) == 0) or (tmp[-1] != '('):
                return 0
            else: # ()
                tmp.pop()
        elif s==']':
            if (len(tmp) == 0) or tmp[-1] != '[':
                return 0
            else: # []
                tmp.pop()
        elif s=='}':
            if (len(tmp) == 0) or tmp[-1] != '{' :
                return 0
            else: # {}
                tmp.pop()
                
    if len(tmp) == 0:
        return 1
    else:
        return 0