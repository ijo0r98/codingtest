# 2908. 상수

# 내 풀이
n, m = map(str, input().split())

def answer(n, m):
    if n[2] > m[2]:
        return n
    elif n[2] < m[2]:
        return m
    else:
        if n[1] > m[1]:
            return n
        elif n[1] < m[1]:
            return m
        else:
            if n[0] > m[0]:
                return n
            elif n[0] < m[0]:
                return m
            
        
print(answer(n, m)[::-1])


# 짱 짧은 다른 사람 풀이
print(max(input()[::-1].split()))

# 다른 사람 풀이2
a, b = input().split()

a = int(a[::-1]) 
b = int(b[::-1])

if a > b : 
    print(a)
else :
    print(b)

