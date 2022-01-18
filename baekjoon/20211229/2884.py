h, m = map(int, input().split())

if m - 45 >= 0:
    m -= 45
else:
    m = m + 60 - 45
    h = h - 1 if h > 0 else 24 - 1

print(h, m)