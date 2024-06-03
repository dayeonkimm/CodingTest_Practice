def solution(d, budget):
    d.sort()
    amount=0
    answer = 0
    for i in d:
        amount += i
        answer += 1
        if amount >= budget:
            break
    if amount <= budget:
        return answer
    else:
        return answer-1
    
    

                
    
        