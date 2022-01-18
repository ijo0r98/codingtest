from math import ceil

# 12 / 5 = 2 .. 2

print(ceil(12/5)) # 3, 나눗셈 후 몫 반올림
print(12//5) # 2, 나눗셈 후 몫 반환
print(-12//5) # -3, 분자가 음수일 경우 양수일때보다 절댓값이 커짐
print(-(-12//5)) # 3
print(-(12//-5)) # 3