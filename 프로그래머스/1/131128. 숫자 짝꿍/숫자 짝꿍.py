def solution(X, Y):
    answer = ''
    for i in range(9,-1,-1):
        x=X.count(str(i))
        y=Y.count(str(i))
        answer += min(x,y)*str(i)
    
    if answer == "":
        return "-1"
    elif set(answer) == {'0'}:
        return "0"
    return answer