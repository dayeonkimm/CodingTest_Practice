def solution(sizes):
    garo = []
    sero = []
    for i in sizes:
        garo.append(max(i))
        sero.append(min(i))
    answer = max(garo)*max(sero)
    return answer