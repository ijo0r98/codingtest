n = input()

m = n
if len(n) == 1:
    n = '0' + n
cnt = 1
tmp = str(int(n[0]) + int(n[1]))
new_n = n[-1] + tmp[-1]
while True:
    if int(new_n) == int(m):
        break
    n = new_n
    tmp = str(int(n[0]) + int(n[1])) 
    new_n = n[-1] + tmp[-1]
    
    cnt += 1

print(cnt)