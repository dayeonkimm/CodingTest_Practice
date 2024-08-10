def solution(myString):
    answer = ''
    for str in myString:
        if str < "l":
            answer += "l"
        else:
            answer += str
    return answer