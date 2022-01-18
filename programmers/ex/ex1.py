# 수식 계산

# 1 * 1 0 * 1 0
def solution(s):
    tmp = [s[0]]
    symbols = ['+', '-', '*', '/']
    for i in range(1, len(s)):
        tmp.append(s[i])
        if (s[i] not in symbols) & (s[i-1] not in symbols): # 숫자일 때
            a = tmp.pop() # 뒤의 숫자
            b = tmp.pop() # 앞의 숫자
            tmp.append(int(str(b)+str(a)))
        elif s[i-1] == '*':
            a = tmp.pop() # 뒤의 숫자 
            tmp.pop() # *
            b = tmp.pop() # 앞의 숫자
            tmp.append(int(b) * int(a))
        elif s[i-1] == '/':
            a = tmp.pop() # 뒤의 숫자
            tmp.pop() # /
            b = tmp.pop() # 앞의 숫자
            tmp.append(int(b) / int(a))

    answer = int(tmp[0])
    for i in range(len(tmp)):
        if tmp[i] == '+':
            answer = answer + int(tmp[i+1])
        elif tmp[i] == '-':
            answer = answer - int(tmp[i+1])
        else: 
            continue

    return answer


# while True:
#     s = input()
#     if s == 'q':
#         break
#     print(solution(s))

print('1 * 10 * 10 = ')
print(solution('1*10*10')) # 100
print('1 + 2 + 3 * 2 + 4 / 2 = ')
print(solution('1+2+3*2+4/2')) # 11
print('2 + 3 + 4 / 1 + 3 * 3 * 3 * 2 + 4 / 2 / 2 + 10 - 5 = ')
print(solution('2+3+4/1+3*3*3*2+4/2/2+10-5')) # 69