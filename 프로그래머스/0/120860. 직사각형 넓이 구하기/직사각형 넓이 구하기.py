def solution(dots):
    a = []
    b = []
    for dot in dots:
        a.append(dot[0])
        b.append(dot[1])
    answer = (max(a)-min(a))*((max(b)-min(b)))
    return answer