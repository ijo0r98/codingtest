# 코딩테스트 연습 > 연습문제 > 행렬의 덧셈

# 1
def solution(arr1, arr2):
    answer = []
    for i in range(len(arr1)):
        temp = []
        for j in range(len(arr1[0])):
            temp.append(arr1[i][j] + arr2[i][j])
        answer.append(temp)

    return answer

# 2
def solution(A,B):
    answer = [[c + d for c, d in zip(a, b)] for a, b in zip(A,B)]
    return answer


print(solution([[1,2],[2,3]], [[3,4],[5,6]]))
print(solution([[1], [2]], [[3],[4]]))