def solution(s):
    num_s = s.count("p") + s.count("P")
    num_y = s.count("y") + s.count("Y")
    if num_s == num_y:
        answer = True
    else:
        answer = False
    return answer