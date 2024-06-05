def solution(my_string):
    answer = list(i for i in my_string.split(" ") if i != "")
    return answer