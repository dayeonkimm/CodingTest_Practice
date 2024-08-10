def solution(my_string):
    answer = []
    for i in range(len(my_string)):
        answer.append(my_string[i-1:])
    answer.sort()
    return answer