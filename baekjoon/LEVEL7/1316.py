# 1316 그룹 단어 체커

n = int(input())

answer = 0
for i in range(n):
    word = list(input())
    tmp = set()
    tmp.add(word[0])
    ck = True
    for i in range(1, len(word)):
        if word[i] not in tmp:
            tmp.add(word[i])
        else: # in tmp
            if word[i] != word[i-1]:
                ck = False
                break
    if ck:
        answer += 1    
            
print(answer)