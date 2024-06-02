import sys

T = int(input())
answer = []

for i in range(T):
    n = int(input())
    n1 = int(n/5)
    n2 = int(n%5)
    # print(("++++"*n1) + " " + ("|"*n2))
    answer.append(("++++"*n1) + " " + ("|"*n2))

for i in range(T):
    print(answer[i])
    

