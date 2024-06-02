def solution(n):
    answer = []
    i = 1
    while 2*i-1 <= n:
        answer.append(2*i-1)
        i+=1
    return answer