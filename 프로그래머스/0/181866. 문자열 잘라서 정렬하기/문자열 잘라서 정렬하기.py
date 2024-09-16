def solution(myString):
    answer = list(myString.split("x"))
    answer2 = []
    for i in answer:
        if i != "":
            answer2.append(i)
    answer2.sort()
    return answer2