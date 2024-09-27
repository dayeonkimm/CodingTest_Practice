def solution(my_strings, parts):
    answer = ''
    for i,k in zip(my_strings, parts):
        answer += i[k[0]:k[1]+1]
    return answer