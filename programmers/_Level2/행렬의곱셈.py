# 코딩테스트 연습 > 연습문제 > 행렬의 곱셈

# Level1. 행렬의 덧셈
def matrix_sum(arr1, arr2):
    answer = []
    for i in range(len(arr1)):
        temp = []
        for j in range(len(arr1[0])):
            temp.append(arr1[i][j] + arr2[i][j])
        answer.append(temp)

    return answer

# Level2. 행렬의 곱셈
# arr1 * arr2 = arr3 일때, arr3[i][j] = arr1[i][:] * arr2[:][j]
def solution(arr1, arr2):
    # answer = [[0 for _ in range(len(arr2[0]))]] * len(arr1) # *으로 복사하여 추가하면 모두 동일한 배열(행)로 취급됨
    answer = [[0 for _ in range(len(arr2[0]))] for _ in range(len(arr1))] # 정답 행렬 0으로 초기화

    for i in range(len(arr1)):
        for j in range(len(arr2[0])):
            for k in range(len(arr1[0])):
                answer[i][j] += (arr1[i][k] * arr2[k][j])
                
    return answer


def solution(A, B):
    return [[sum(a*b for a, b in zip(A_row,B_col)) for B_col in zip(*B)] for A_row in A]



print(solution([[1, 4], [3, 2], [4, 1]], [[3, 3], [3, 3]])) # [[15, 15], [15, 15], [15, 15]]
print(solution([[2, 3, 2], [4, 2, 4], [3, 1, 4]], [[5, 4, 3], [2, 4, 1], [3, 1, 1]])) # [[22, 22, 11], [36, 28, 18], [29, 20, 14]]