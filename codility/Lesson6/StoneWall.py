# 0129

# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

# H[i] i~i+1 높이
# 벽을 구성하는 최소의 직사각형 수

# 1 -> 42%
def solution(H):
    answer = 1
    height = set()
    past = H[0]
    for i in range(1, len(H)):
        if past > H[i]: # 높이가 작아지면 사각형이 바뀜
            past = H[i]
            answer += 1
            answer += len(height)
            height = set()
        elif past < H[i]: # 높이가 계속 같거나 커지는 경우 일단 진행
            height.add(H[i])

    return answer + len(height)