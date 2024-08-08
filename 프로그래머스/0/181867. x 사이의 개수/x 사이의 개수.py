def solution(myString):
    answer = []
    x_list = myString.split("x")
    for i in x_list:
        answer.append(len(i))
    return answer