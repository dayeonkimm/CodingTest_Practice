def solution(board, h, w):
    answer = 0
    n = len(board)
    dh = [0,1,-1,0]
    dw = [1,0,0,-1]
    for i in range(4):
        a=h+dh[i]
        b=w+dw[i]
        if 0<=a<n and 0<=b<n:
            if board[a][b] == board[h][w]:
                answer +=1
    return answer