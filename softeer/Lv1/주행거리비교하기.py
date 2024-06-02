import sys

inputs = list(map(int, input().split(" ")))
a, b = inputs[0], inputs[1]

if a==b : print("same")
elif a>b : print("A")
else : print("B")