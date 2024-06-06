def solution(s):
    answer = ""
    str_ls = list(s.split(" "))
    for i in range(len(str_ls)):
        for j in range(len(str_ls[i])):
            if j%2 == 0:
                answer += str_ls[i][j].upper()
            else:
                answer += str_ls[i][j].lower()
        answer += " "
    return answer[:-1]