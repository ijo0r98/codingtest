# 코딩테스트 연습 > 연습문제 > 제일 작은 수 제거하기

def solution(arr):
    # m = min(arr)
    # arr.pop(arr.index(m))
    arr.pop(arr.index(min(arr)))
    if len(arr) == 0:
        return [-1]
    else:
        return arr

def solution(arr):
    arr.remove(min(arr))
    return [-1] if len(arr) == 0 else arr

print(solution([4, 3, 2, 1])) # [4, 3, 2]