# 2941 크로아티아 알파벳

# ljes=njak

inputs = input()

# c=, c-, dz=, d-, lj, nj, s=, z=
# answer = 0 
# inputs.reverse()
# while inputs:
#     i = inputs.pop()
#     answer += 1
#     try:
#         if i == 'c':
#             if (inputs[-1] == '=') or (inputs[-1]=='-'):
#                 inputs.pop()
#         elif i == 'd':
#             if (inputs[-1] == '-'):
#                 inputs.pop()
#             elif (inputs[-1]=='z') and (inputs[-2]=='='):
#                 inputs.pop()
#                 inputs.pop()
#         elif i == 'l':
#             if (inputs[-1]=='j'):
#                 inputs.pop()
#         elif i == 'n':
#             if (inputs[-1]=='j'):
#                 inputs.pop()
#         elif i == 's':
#             if (inputs[-1]=='='):
#                 inputs.pop()
#         elif i == 'z':
#             if (inputs[-1]=='='):
#                 inputs.pop()
#     except:
#         break

# print(answer)

words = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
for word in words:
    inputs = inputs.replace(word, '*')
print(len(inputs))