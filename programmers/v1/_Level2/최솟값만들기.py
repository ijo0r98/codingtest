# 코딩테스트 연습 > 연습문제 > 최솟값 만들기

# 정렬 -> 최소 * 최대
# 왜 이렇게 되는지는 잘 모르겠음..

def solution(A, B):
    answer = 0
    A.sort()
    B.sort()

    for i in range(len(A)):
        answer += A[i] * B[len(A) - i - 1]

    return answer

def solution(A, B):
    return sum(a*b for a, b in zip(sorted(A), sorted(B, reverse = True)))


print(solution([1, 4, 2], [5, 4, 4]	)) # 29