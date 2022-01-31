# 코딩테스트 연습 > 2019 카카오 개발자 겨울 인턴십 > 크레인 인형뽑기 게임

# 내 풀이
def solution(board, moves):
    answer = 0
    out_list = []
    board_dict = {}
    for i in range(0, len(board)):
        board_dict[i] = []
    
    # 주어진 2차원 배열 -> 각 열마다 stack
    for nums in board:
        for i, num in enumerate(nums):
            if num != 0:
                board_dict[i].append(num)      

    for m in moves:
        if (board_dict[m-1]):
            out = board_dict[m-1].pop(0)
            
            if len(out_list) == 0:
                out_list.append(out)
                continue

            if out == out_list[-1]:
                out_list.pop()
                answer += 2
            else:
                out_list.append(out)

    return answer


# 다른 사람 풀이 1
def solution(board, moves):
    stacklist = [] # 꺼낸 인형
    answer = 0

    for i in moves:
        for j in range(len(board)):
            if board[j][i-1] != 0:
                stacklist.append(board[j][i-1])
                board[j][i-1] = 0 # i -> 꺼낼 열의 번호, j -> 위(앞)에서부터 제거

                if len(stacklist) > 1: # 1개 이상 꺼냈을 때
                    if stacklist[-1] == stacklist[-2]: # 추가한 인형과 가장 최근에 담은 인형이 같을 때
                        stacklist.pop(-1) # 둘 다 삭제
                        stacklist.pop(-1) 
                        answer += 2     
                break

    return answer


print('answer: ', solution([[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]], [1,5,3,5,1,2,1,4])) # 4
