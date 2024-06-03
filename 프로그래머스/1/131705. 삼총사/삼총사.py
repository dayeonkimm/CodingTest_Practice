from itertools import combinations

def solution(number):
    answer = 0
    combi_list = list(combinations(number,3))
    for combi in combi_list:
        if sum(combi) == 0:
            answer += 1
    return answer