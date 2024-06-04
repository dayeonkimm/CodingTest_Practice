def solution(left, right):
    answer = 0
    for i in range(left, right+1):
        div_num = 0
        for j in range(1,i+1):
            if i%j==0:
                div_num +=1  
        if div_num%2 ==0:
            answer += i
        else:
            answer -= i
    return answer