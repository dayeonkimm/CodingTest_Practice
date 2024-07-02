def solution(X, Y):
    answer = ''
    for i in range(0,10):
        x=X.count(str(i))
        y=Y.count(str(i))
        answer += min(x,y)*str(i)
    answer = sorted(list(answer),reverse=True)
    answer = "".join(answer)
    if answer == "":
        return "-1"
    elif set(answer) == {'0'}:
        return "0"
    return answer