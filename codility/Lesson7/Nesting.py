# 0129

# 1 -> 100%
def solution(S):
    brackets = []
    for s in S:
        if (s=='('):
            brackets.append(s)
        else:
            if (len(brackets) == 0): # 열린 괄호가 없음
                return 0
            else: # 열린 괄호가 있음
                brackets.pop()

    if len(brackets) == 0:
        return 1
    else:
        return 0