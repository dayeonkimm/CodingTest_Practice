def solution(my_string):
    moem = ["a","e","i","o","u"]
    answer = ''
    for i in my_string:
        if i not in moem:
            answer += i
    return answer