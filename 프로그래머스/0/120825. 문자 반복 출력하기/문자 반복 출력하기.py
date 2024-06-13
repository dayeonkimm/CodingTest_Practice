def solution(my_string, n):
    answer = ''
    for i in my_string:
        answer += n*i
    return answer