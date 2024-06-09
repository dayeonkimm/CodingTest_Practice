def solution(n, m):
    a = min(n,m) 
    b = max(n,m)
    answer = []
    divs = []
    
    for i in range(1,b+1):
        if b%i == 0:
            divs.append(i)
    for div in divs[::-1]:
        for j in range(1,a+1):
            if (a%j == 0) and j == div:
                answer.append(j)
                answer.append(a*b/j)
                return answer
    
    