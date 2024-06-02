def solution(n):
    n = str(n)
    number = list(n)
    answer = 0
    for i in number:
        answer += int(i)
    return answer