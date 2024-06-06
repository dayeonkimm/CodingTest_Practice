def solution(s):
    num_ls = []
    for num in s.split(" "):
        num_ls.append(int(num))
    answer = str(min(num_ls))+ " " + str(max(num_ls))
    return answer