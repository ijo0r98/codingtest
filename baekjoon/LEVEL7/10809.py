# 10809. 알파벳 찾기

s = input()
alphabets = [chr(i) for i in range(97, 97 + 26)]
answer = ''
for alphabet in alphabets:
    if len(answer) != 0:
        answer += (' ' + str(s.find(alphabet)))
    else:
        answer += str(s.find(alphabet))
print(answer)