def solution(A,B):
    A.sort()
    B.sort()
    answer = 0
    
    for i,j in zip(A,B[::-1]):
        answer += i*j
        
    return answer