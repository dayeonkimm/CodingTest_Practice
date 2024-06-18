def solution(n, m, section):
    answer = 1
    start = section[0]
    if len(section) == 1:
        return answer
    for i in section[1:]:
        if i-start >= m:
            answer += 1
            start = i
        else:
            pass
    return answer