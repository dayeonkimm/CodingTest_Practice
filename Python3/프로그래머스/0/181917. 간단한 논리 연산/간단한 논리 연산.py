def solution(x1, x2, x3, x4):
    if x1 == True or x2 == True:
        y1 = True
    else:
        y1 = False
    if x3 == True or x4 == True:
        y2 = True
    else:
        y2 = False
    if y1 == False or y2 == False:
        return False
    else:
        return True