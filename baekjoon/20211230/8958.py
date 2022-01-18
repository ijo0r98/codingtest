n = int(input())

cnt = 0
for i in range(n):
    result = input()
    total = 0
    cnt = 0
    for j in range(len(result)):
        if result[j] == 'O':
            cnt += 1
            total += cnt
        elif result[j] == 'X':
            cnt = 0
        
    print(total)