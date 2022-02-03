# 브루트 포스(완전탐색) > 체스판 다시 칠하기

n, m = map(int, input().split())
board = []
answer = 100

for i in range(n):
    board.append(list(input()))

for i in range(0, n-7):
    for j in range(0, m-7):
        cnt1, cnt2 = 0, 0
        # color = board[i][j] # 가장 왼쪽 위의 color
        color1 = 'B'
        color2 = 'W'
        for k in range(i, i+8):
            for l in range(j, j+8):
                # print((k-i), (l-j))
                if ((k-i)+(l-j)) % 2 == 0 :
                    if board[k][l] != color1:
                        cnt1 += 1
                    if board[k][l] != color2:
                        cnt2 += 1
                else:
                    if board[k][l] == color1:
                        cnt1 += 1
                    if board[k][l] == color2:
                        cnt2 += 1
        
        answer = min(answer, min(cnt1, cnt2))
        
print(answer)
                                
            