def solution(A, B):
    new = A
    answer = 0
    if A == B:
        return 0
    for i in range(len(A)-1):
        new = new[-1]+new[0:len(A)-1]
        answer += 1
        if new == B:
            return answer
    return -1