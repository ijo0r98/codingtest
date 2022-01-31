# 완전탐색 > 카펫.py

def solution(brown, yellow):
    # 전체 가로세로 길이 = 노란색 가로세로 길이 + 2

    answer = []

    # 1. 노란색 타일 수의 약수 튜플 리스트 -> 만들어질 수 있는 사각형의 형태
    divisors = []
    for i in range(1, int(yellow ** (1/2) + 1)): # (가로, 세로) 가로 >= 세로
        if yellow % i == 0:
            divisors.append((int(yellow/i), i))

    # 2. 갈색 타일이 사각형을 감싸는 모양임으로 노란색 타일 사각형 가로세로 길이로 갈색 사각형 길이 계산 가능
    for d in divisors:
        brown_cnt = 0
        print(d)
        brown_cnt += (d[0] + 2) * 2 # 가로 2줄
        brown_cnt += (d[1]) * 2 # 세로 2줄

        if brown_cnt == brown:
            # 3. 각 노란색 사각형일때 구한 갈색 타일 수가 알맞을 때 전체 사각형의 가로, 세로 길이 구함
            answer = (d[0]+2, d[1]+2)
            return answer



# print('answer : ', solution(10, 2)) # [4, 3]
# print('answer : ', solution(8, 1)) # [3, 3]
print('answer : ', solution(24, 24)) # [8, 6]