n = int(input())
cnt = 0
lst=[500,100,50,10] # 거스름돈 종류

for i in lst:
  cnt += n // i
  n %= i

print(cnt)