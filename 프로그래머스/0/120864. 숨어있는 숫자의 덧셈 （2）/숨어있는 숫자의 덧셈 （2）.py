def solution(my_string):
    num = ""
    answer = 0
    for i in my_string:
        if i.isdigit():
            num += i
        else:
            num += " "
    for j in num.split():
        answer += int(j)
    return answer