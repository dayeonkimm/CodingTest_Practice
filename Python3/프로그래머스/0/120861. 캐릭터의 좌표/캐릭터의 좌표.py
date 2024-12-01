def solution(keyinput, board):
    a = (board[0]-1)//2
    b = (board[1]-1)//2
    c = 0
    d = 0
    for i in keyinput:
        if i == "left":
            c -= 1
            c = max(c,-a)
        elif i == "right":
            c += 1
            c = min(c,a)
        elif i == "up":
            d += 1
            d = min(d,b)
        else:
            d -= 1
            d = max(d, -b)
    return [c,d]