def solution(order):
    answer = 0
    for i in str(order):
        if ("3" in i) or ("6" in i) or ("9" in i):
            answer += 1
    return answer