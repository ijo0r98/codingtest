n = int(input())

for i in range(n):
    arr = list(map(int, input().split()))
    avg = sum(arr[1:]) / arr[0]
    cnt = 0
    for a in arr[1:]:
        cnt = cnt + 1 if a > avg else cnt  
    print("{:.3f}%".format(cnt/arr[0]*100))
        
# 11 0 -> 0.000%