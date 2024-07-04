def solution(N, stages):
    answer = {}
    count = 0
    for i in range(1,N+1):
        if len(stages)-count == 0:
            answer[i] = 0
        else:
            answer[i] = stages.count(i)/(len(stages)-count)
            count += stages.count(i)
    answer2 = sorted(answer, key=lambda x: answer[x], reverse=True)
    
    # answer = sorted(answer.items(), key = lambda x: (-x[1], x[0]))
    # answer2 = [t[0] for t in answer]
    return answer2