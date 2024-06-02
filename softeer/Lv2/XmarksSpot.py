import sys
sys.setrecursionlimit(5000)

# n = int(input())
# answer = ""
# for i in range(n):
#     inputs = input().split(" ")
#     s, t = inputs[0].upper(), inputs[1].upper()

#     index = s.index("X")
#     answer+=t[index]

# for i in range(n):
#     inputs = input().split()
#     for i in range(len(inputs[0])):
#         if inputs[0][i].upper()=='X':
#             answer+=inputs[1][i].upper()
#             break
        
# print(answer)
        
N = int(input())
answer = []
for _ in range(N):
    S, T = map(str, input().split())
    for i, s in enumerate(S):
        if s == 'x' or s == 'X':
            answer.append(T[i].upper())
            break

print(''.join(answer))



