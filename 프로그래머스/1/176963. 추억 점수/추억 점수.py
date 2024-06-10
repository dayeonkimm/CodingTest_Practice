def solution(name, yearning, photo):
    ny_dic = dict(zip(name,yearning))
    answer = []
    for i in photo:
        sum = 0
        for j in i:
            if j in ny_dic.keys():
                sum += ny_dic[j]
        answer.append(sum)   
    return answer