def solution(my_string):
    new = list(my_string.lower())
    new.sort()
    answer = ""
    for i in new:
        answer += i
    return answer