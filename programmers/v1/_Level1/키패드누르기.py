# 코딩테스트 연습 > 2020 카카오 인턴십 > 키패드 누르기

# 1, 4, 7 -> L
# 3, 6, 9 -> R
# 2, 5, 8 -> L/R

# 내 풀이
def solution(numbers, hand):
    answer = ''
    left = 10
    right = 12

    for n in numbers:
        # print('left : ', left, ' right : ', right, ' n : ', n)

        if n == 0:
            n = 11
            
        if n in (1, 4, 7, 10):
            left, answer = useLeft(left, n, answer)
        elif n in (3, 6, 9, 12):
            right, answer = useRight(right, n, answer)
        else: 
            left_d = abs(n - left) # n과의 상대적 위치를 비교하기 위해
            right_d = abs(n - right)
            left_d = (left_d % 3) + (left_d // 3) # 키패드 가로 길이가 3임을 이용하여 위치 계산
            right_d = (right_d % 3) + (right_d // 3)

            # print('left_d : ', left_d, ' right_d : ', right_d, ' n : ', n)

            if left_d < right_d:
                left, answer = useLeft(left, n, answer)
            elif right_d < left_d:
                 right, answer = useRight(right, n, answer)
            else:
                if hand == "right":
                    right, answer = useRight(right, n, answer)
                else:
                    left, answer = useLeft(left, n, answer)

    return answer

def useRight(right, n, answer):
    right = n
    answer += 'R'
    return right, answer

def useLeft(left, n, answer):
    left = n
    answer += 'L'
    return left, answer



print('answer: ', solution([1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5], 'right')) # "LRLLLRLLRRL"
# print('answer: ', solution([7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2], 'left')) # "LRLLRRLLLRR"
# print('answer: ', solution([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]	, 'right')) # "LLRLLRLLRL"
