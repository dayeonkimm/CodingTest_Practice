def solution(k, m, score):
    score.sort(reverse=True)
    answer = 0
    for i in range(len(score)//m):
        answer += m*score[m*(i+1)-1]
    return answer