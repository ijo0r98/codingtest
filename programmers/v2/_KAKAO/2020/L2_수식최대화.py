# 2020 카카오 인턴십 > 수식 최대화

from itertools import permutations

def solution(expression):
    answer = []
    operators = set()
    
    ex2 = []
    k = 0
    for i in range(len(expression)):
        if expression[i] in ['+', '-', '*']:
            operators.add(expression[i])
            ex2.append(int(expression[k:i]))
            ex2.append(expression[i])
            k = i+1
    ex2.append(int(expression[k:]))
    operate_order = list(permutations(operators))
    
    for order in operate_order:
        ex = ex2.copy()
        for opr in order:
            while opr in ex:
                i = ex.index(opr)
                if opr == '*':
                    ex[i-1] = ex[i-1] * ex[i+1]
                elif opr =='-':
                    ex[i-1] = ex[i-1] - ex[i+1]
                elif opr == '+':
                    ex[i-1] = ex[i-1] + ex[i+1]
                ex = ex[:i] + ex[i+2:]
        answer.append(abs(ex[0]))
    
    return max(answer)


# 다른 사람 풀이
def solution(expression):
    operations = [('+', '-', '*'),('+', '*', '-'),('-', '+', '*'),('-', '*', '+'),('*', '+', '-'),('*', '-', '+')]
    answer = []
    for op in operations:
        a = op[0]
        b = op[1]
        temp_list = []
        for e in expression.split(a):
            temp = [f"({i})" for i in e.split(b)]
            temp_list.append(f'({b.join(temp)})')
        answer.append(abs(eval(a.join(temp_list))))
    return max(answer)
