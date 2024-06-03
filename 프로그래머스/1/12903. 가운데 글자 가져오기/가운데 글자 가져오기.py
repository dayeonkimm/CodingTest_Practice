def solution(s):
    n = int(len(s)/2)
    if len(s)%2  == 0:
        answer = s[n-1:n+1]
    else:
        answer = s[n]
    return answer



# def solution(str):
#     return str[(len(str)-1)//2 : len(str)//2 + 1]
