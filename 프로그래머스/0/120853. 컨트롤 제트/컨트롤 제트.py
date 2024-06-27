def solution(s):
    s_list = list(s.split())
    answer = 0
    for i in s_list:
        if i != "Z":
            answer += int(i)
            last = int(i)
        else:
            answer -= last
    return answer