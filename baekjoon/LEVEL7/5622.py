# 5622. 다이얼

# 숫자 1 -> 2초, 2 -> 3초 .. 9 -> 10초, 0 -> 11초 

inputs = input()

answer = 0
alpabets = ['ABC','DEF','GHI','JKL','MNO','PQRS','TUV','WXYZ']
# alpabets_ascii = [ord('A'), ord('D'), ord('G'), ord('J'), ord('M'), ord('P'), ord('T'), ord('W')]
for s in inputs:
    for dial, alpabet in enumerate(alpabets):
        if s in alpabet:
            answer += (dial + 3) 
            
print(answer)

