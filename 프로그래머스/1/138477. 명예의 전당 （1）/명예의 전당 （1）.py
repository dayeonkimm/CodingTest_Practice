def solution(k, score):
    answer = []
    for i in range(len(score)):
        if i<k:
            answer.append(min(score[:i+1]))
        else:
            score_list = score[:i+1]
            score_list.sort(reverse=True)
            answer.append(score_list[k-1])
    return answer