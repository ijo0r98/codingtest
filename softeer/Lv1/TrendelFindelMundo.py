import sys

N = int(input())

answer_x, answer_y = 1001, 1001
for i in range(N):
    inputs = input()
    x=int(inputs.split(" ")[0])
    y=int(inputs.split(" ")[1])
    
    if(y < answer_y) :
        answer_y = y
        answer_x = x

print(answer_x, answer_y)
