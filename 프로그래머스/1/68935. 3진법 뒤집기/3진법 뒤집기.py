def solution(n):
    answer = 0
    ls = []
    while n>=3:
        ls.append(n%3)
        n=n//3
    ls.append(n)
    ls.reverse()
    
    for i in range(len(ls)):
        answer += ls[i]*(3**i)
          
    return answer