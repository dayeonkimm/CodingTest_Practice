def solution(my_string):
    answer = []
    for i in my_string:
        try:
            int(i)
            answer.append(int(i))
        except:
            pass
    answer.sort()
    return answer