# 코딩테스트 연습 > 2020 KAKAO BLIND RECRUITMENT > 문자열 압축

def solution(s):
    answer = []
    answer_s = ''
    for i in range(1, len(s) + 1): # 자를 문자열의 길이 2 ~ (전체-1)
        tmp = s[0:i]
        cnt = 1
        j = i 
        while True:
            compare = s[j:j+i]
            if tmp == compare:
                # print('== ', cnt, tmp, compare)
                cnt += 1
            else:
                # print('!= ', cnt, tmp, compare)
                answer_s = answer_s + str(cnt) + tmp if cnt > 1 else answer_s + tmp
                cnt = 1
                tmp = compare
            j += i
            
            if len(s[j-i-1:]) < i:
                answer_s += tmp
                # print('answer_s: ', answer_s)
                answer.append(len(answer_s))
                answer_s = ''
                break

    return min(answer)


print('answer: ', solution('aabbaccc')) # 7 2a2ba3c
print('answer: ', solution('ababcdcdababcdcd')) # 9 2ababcdcd
print('answer: ', solution('abcabcdede')) # 8 2abcdede
print('answer', solution('a')) # 1
