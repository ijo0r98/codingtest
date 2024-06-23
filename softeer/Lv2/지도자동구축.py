import sys

n = int(input())

# 0 > 2
# 1 > 3= 2+1 = 2+2^0
# 2 > 5= 3+2 = 3+2^1
# 3 > 9= 5+4 = 5+2^2

res=2
for i in range(1,n+1):
    # print(res, i, 2**(i-1))
    res += 2**(i-1)
    
print(res*res)
