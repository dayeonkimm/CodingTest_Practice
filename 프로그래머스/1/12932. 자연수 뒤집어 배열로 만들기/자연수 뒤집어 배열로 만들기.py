def solution(n):
    n = str(n)
    num_list = list(n)
    answer = []
    for i in num_list:
        answer.insert(0,int(i))
    return answer