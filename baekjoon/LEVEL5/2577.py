a = int(input())
b = int(input())
c = int(input())

total = str(a * b * c)

num_cnt = [0 for i in range(10)]
for i in range(len(total)):
    num_cnt[int(total[i])] +=1

for cnt in num_cnt:
    print(cnt)