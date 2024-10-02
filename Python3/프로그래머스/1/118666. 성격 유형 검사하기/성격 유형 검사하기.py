def solution(survey, choices):
    kdic = {"R":0,"T":0,"C":0,"F":0,"J":0,"M":0,"A":0,"N":0}
    answer = ''
    for i,j in zip(survey,choices):
        if j==1:
            kdic[i[0]]+=3
        elif j==2:
            kdic[i[0]]+=2
        elif j==3:
            kdic[i[0]]+=1
        elif j==5:
            kdic[i[1]]+=1
        elif j==6:
            kdic[i[1]]+=2
        elif j==7:
            kdic[i[1]]+=3
    if kdic["R"]>=kdic["T"]:
        answer+="R"
    else:
        answer+="T"
    if kdic["C"]>=kdic["F"]:
        answer+="C"
    else:
        answer+="F"
    if kdic["J"]>=kdic["M"]:
        answer+="J"
    else:
        answer+="M"
    if kdic["A"]>=kdic["N"]:
        answer+="A"
    else:
        answer+="N"
    return answer