def solution(s):
    s1=sorted(s)
    answer = ''
    for str in s1:
        if str not in answer:
            if s1.count(str) == 1:
                answer += str
    return answer