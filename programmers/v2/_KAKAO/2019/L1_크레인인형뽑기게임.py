# 2019 카카오 개발자 겨울 인턴십 > 크레인 인형뽑기 게임

# 1
def solution(board, moves):
    answer = 0
    basket = []
    N = len(board)
    new_board = [[] for i in range(N)]
    
    for i in range(N):
        for j in range(N):
            if board[i][j] != 0:
                new_board[j].append(board[i][j])

    for i in range(N):
        new_board[i].reverse()
    
    for move in moves:
        if new_board[move-1]:
            new = new_board[move-1][-1]
            new_board[move-1].pop()

            if not basket:
                basket.append(new)
            else:
                if new == basket[-1]:
                    answer += 2
                    basket.pop()
                else:
                    basket.append(new)
        
    return answer


# 다른 사람 풀이 
def solution(board, moves):
    stacklist = []
    answer = 0

    for i in moves:
        for j in range(len(board)):
            if board[j][i-1] != 0:
                stacklist.append(board[j][i-1])
                board[j][i-1] = 0

                if len(stacklist) > 1:
                    if stacklist[-1] == stacklist[-2]:
                        stacklist.pop(-1)
                        stacklist.pop(-1)
                        answer += 2     
                break

    return answer
