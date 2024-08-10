def solution(myString):
    answer = ''
    for str in myString:
        if str in ["a","b","c","d","e","f","g","h","i","j","k"]:
            answer += "l"
        else:
            answer += str
    return answer