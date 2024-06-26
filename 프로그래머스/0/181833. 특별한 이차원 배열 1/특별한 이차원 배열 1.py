def solution(n):
    answer = []
    for i in range(n):
        mini = [0]*n
        mini[i]=1
        answer.append(mini)
    return answer
        
        