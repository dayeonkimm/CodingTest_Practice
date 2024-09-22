def solution(intStrs, k, s, l):
    answer = []
    for i in intStrs:
        op = int(i[s:s+l])
        if op > k:
            answer.append(op) 
    return answer