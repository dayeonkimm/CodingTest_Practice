def solution(myString):
    answer = ''
    for i in myString:
        if i in ["a","A"]:
            answer += i.upper()
        else:
            answer += i.lower() 
    return answer