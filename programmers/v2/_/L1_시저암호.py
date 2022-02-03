# 연습문제 > 시저암호

# 1 tmp에 n 더하기 전에 확인해야함
def solution(s, n):
    # print(ord('A'), ord('Z'), ord('a'), ord('z')) # 65 90 97 122
    answer = ''
    for i in range(len(s)):
        if s[i] != ' ':
            tmp = ord(s[i]) + n
            # print(s[i], ord(s[i]), tmp, chr(tmp))
            if (tmp > 122) or ((tmp > 90) and (tmp < 97)):
                print('after ', tmp-26, chr(tmp-26))
                tmp -= 26
            answer += chr(tmp)
        else:
            answer += s[i]
        
    return answer

# 2 잘못된 풀이
def solution(s, n):
    # print(ord('A'), ord('Z'), ord('Y'), ord('a'), ord('z')) # 65 90 97 122
    
    answer = ''
    for i in range(len(s)):
        if s[i] != ' ':
            tmp = ord(s[i])
            if (s[i] >= 'Z') or (s[i] >= 'z'):
                tmp -= 26
            answer += chr(tmp + n)
        else:
            answer += s[i]
        
    return answer


# 3 Z->A로 넘어갈 때 범위를 넘어가 [a, z] 사이 있어 예외처리가 안되는 경우 파악해야함
def solution(s, n):
    answer = ''
    for i in range(len(s)):
        if s[i] != ' ':
            tmp = ord(s[i]) + n
            if (tmp > 122):
                tmp -= 26
            elif (ord(s[i]) <= 90) and (tmp > 90):
                tmp -= 26
            answer += chr(tmp)
        else:
            answer += s[i]
        
    return answer