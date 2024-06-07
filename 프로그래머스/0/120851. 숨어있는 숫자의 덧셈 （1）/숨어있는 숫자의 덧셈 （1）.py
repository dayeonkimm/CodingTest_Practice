def solution(my_string):
    answer = 0
    for i in my_string:
        try:
            int(i)
            answer += int(i)
        except:
            pass
    return answer