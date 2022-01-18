
# 코딩테스트 연습 > 2021 Dev-Matching: 웹 백엔드 개발자(상반기) > 행렬 테두리 회전하기

# def solution(rows, columns, queries): # 행, 열
#     answer = []
#     matrix = [[j + i * columns for j in range(1, columns + 1)] for i in range(rows)]
#     for q in queries:
#         i, j = q[0], q[1]
#         past = matrix[i-1][j-1]
#         min = past 
#         while True:
#             if (i == q[0]) & (j >= q[1]) & (j < q[3]):
#                 j += 1
#             elif (j == q[3]) & (i >= q[0]) & (i < q[2]):
#                 i += 1
#             elif (i == q[2]) & (j > q[1]) & (j <= q[3]):
#                 j -= 1
#             elif (j == q[1]) & (i > q[0]) & (i <= q[2]):
#                 i -= 1
            
#             if (i == q[0]) & (j == q[1]):
#                 break
            
#             tmp = matrix[i-1][j-1]
#             matrix[i-1][j-1] = past
#             past = tmp

#             if past < min:
#                 min = past
    
#         answer.append(min)

#     print2d(matrix)
#     return answer

# def solution(rows, columns, queries): # 행, 열
#     answer = []
#     matrix = [[j + i * columns for j in range(1, columns + 1)] for i in range(rows)]
#     for q in queries:
#         past = matrix[q[0]][q[1]]
#         min = past 
#         for j in range(q[1], q[3]):
#             matrix[q[0]-1][j-1] = matrix[q[0]-1][j-2]
#             min = min(min, matrix[q[0]-1][j-1])
#         for i in range(q[0], q[2]):
#             matrix[i-1][j-1] = matrix[i-1][j-2]
#             min = min(min, matrix[q[0]-1][j-1])
#         for j in range(q[3], q[1]-1):
#             indexj = j
#             matrix[indexi-1][indexj-1] -= 1
#         for i in range(q[2], q[0], -1):
#             indexi = i
#             matrix[indexi-1][indexj-1] += columns


def solution(rows, columns, queries): # 행, 열
    answer = []
    table = [[j + i * columns for j in range(1, columns + 1)] for i in range(rows)]
    
    for query in queries:
        q = [x-1 for x in query] # 0부터 시작하는 2차원 배열 인덱스에 맞춰 1씩 빼줌
        small = rows * columns
        
        # top -> right
        for j in range(q[1], q[3]):
            tmp = table[q[0]][j-1]
            table[q[0]][j] = tmp
            small = min(small, tmp)
            
        print2d(table)
        print('-----------')
        # right -> bottom
        for i in range(q[0], q[2]):
            tmp = table[i][q[3]]
            table[i][q[3]] = tmp
            small = min(small, tmp)
        print2d(table)
        print('-----------')
        # bottom -> left
        for j in range(q[3], q[1], -1):
            tmp = table[q[2]][j]
            table[q[2]][j] = tmp
            small = min(small, tmp)
        print2d(table)
        print('-----------')
        
        # left -> top
        for i in range(q[2], q[0], -1):
            tmp = table[i][q[1]]
            table[i][q[1]] = tmp
            small = min(small, tmp)
        print2d(table)
            
        answer.append(small)

    return answer


def print2d(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            print(matrix[i][j], end=' ')
        print('\n')

# print(solution(6, 6, [[2,2,5,4]])) # [8]
print(solution(6, 6, [[3, 3, 6, 6]])) # [10]
# print(solution(6, 6, [[2,2,5,4],[3,3,6,6],[5,1,6,3]])) # [8, 10, 25]

