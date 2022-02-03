# 브루트 포스(완전탐색) > 분해합

n = int(input())

# 1
# for i in range(1, n+1):
#     m, tmp = i, i
#     while tmp != 0:
#         m += (tmp%10)
#         tmp //= 10
        
#     if m == n:
#         print(i)
#         break
#     if i == n:
#         print(0)
        
        
# 2
for i in range(1, n+1):
    m = i + sum(map(int, str(i)))
    if m == n:
        print(i)
        break
    if i == n:
        print(0)   