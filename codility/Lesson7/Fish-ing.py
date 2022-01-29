# 0129
# A 물고기 크기
# B 물고기 이동 방향(0은 위로, 1은 아래로)
# 두 물고기가 마주쳤을 때 크기가 더 큰 물고기가 살아남음
# P < Q, B[P] = 1 and B[Q] = 0  앞 물고기 1(아래) -> 뒤 물고기 0(위) 일때 두 물고기가 마주침
# A[P] > A[Q] P(1)가 잡아먹고 계속 내려감(1)
# A[Q] > A[P] Q(0)가 잡아먹고 계속 올라감(0)

# 1 -> 37%
def solution(A, B):
    up = [] # 0
    down = [] # 1
    answer = 0

    for i in range(len(A)):
        answer += 1
        if B[i] == 0: # up
            if len(down)!=0: # 잡아먹힘
                answer -= 1
                if down[-1] > A[i]: # 내려가는 물고기가 더 큼
                    down.append(down[-1])
                else: # 올라가는 물고기가 더 큼
                    up.append(A[i])
            else:
                up.append(A[i])

        else: # down
            down.append(A[i])

    # print('up: ', up)
    # print('down: ', down)

    return answer

# 2 -> 37%
def solution(A, B):
    up = [] # 0
    down = [] # 1
    answer = 0

    for i in range(len(A)):
        answer += 1
        if B[i] == 0: # up
            if len(down)!=0: # 잡아먹힘
                answer -= 1
                if down[-1] < A[i]: # 올라오는 물고기가 더 큼
                    down.pop()
                    up.append(A[i])
            else:
                up.append(A[i])

        else: # down
            down.append(A[i])

    return answer