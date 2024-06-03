from itertools import combinations

def solution(number):
    answer = 0
    combi_list = list(combinations(number,3))
    for combi in combi_list:
        if sum(combi) == 0:
            answer += 1
    return answer


# def solution(number):
#     answer = 0
#     l = len(number)
#     for i in range(l-2):
#         for j in range(i+1, l-1):
#             for k in range(j+1, l):
#                 # print(number[i],number[j],number[k])
#                 if number[i]+number[j]+number[k] == 0:
#                     answer += 1   
#     return answer
