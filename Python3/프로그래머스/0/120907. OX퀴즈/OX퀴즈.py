def solution(quiz):
    answer = []
    for q in quiz:
        a,b=q.split("=")
        x=list(a.split(" "))
        if "+" in x:
            if int(x[0])+int(x[2])==int(b):
                answer.append("O")
            else:
                answer.append("X")
        else:
            if int(x[0])-int(x[2])==int(b):
                answer.append("O")
            else:
                answer.append("X")
    return answer