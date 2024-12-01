def solution(keyinput, board):
    a = (board[0]-1)//2
    b = (board[1]-1)//2
    answer = []
    c = 0
    d = 0
    for i in keyinput:
        if i == "left":
            c -= 1
            if c < -a:
                c = -a
        elif i == "right":
            c += 1
            if c > a:
                c = a
        elif i == "up":
            d += 1
            if d > b:
                d = b
        else:
            d -= 1
            if d < -b:
                d = -b
    return [c,d]