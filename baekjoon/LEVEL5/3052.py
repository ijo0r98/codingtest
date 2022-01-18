last = []
for i in range(10):
    a = int(input())
    if not last:
        last.append(a%42)
    else:
        if a%42 not in last:
            last.append(a%42)
    
print(len(last))