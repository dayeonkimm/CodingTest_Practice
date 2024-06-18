def solution(my_string):
    num = ""
    answer = 0
    for i in my_string:
        if i.isdigit():
            num += i
        else:
            if num != "":
                answer += int(num)
                num = ""
    if num != "":
        answer += int(num)
    return answer