max = 0
idx = 0
for i in range(9):
    a = int(input())
    if a > max:
        idx = i
        max = a

print(max) 
print(idx + 1)