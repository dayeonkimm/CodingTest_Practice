def solution(strings, n): 
    answer = []
    answer2 = []
    for str in strings:
        answer.append(str[n]+str)
    answer.sort()
    for str in answer:
        answer2.append(str[1:])
    return answer2

