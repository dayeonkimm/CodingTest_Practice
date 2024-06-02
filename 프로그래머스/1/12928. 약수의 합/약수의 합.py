def solution(n):
    num_list = []
    for i in range(1,n+1):
        if n%i == 0:
            if i not in num_list:
                num_list.append(i)
            if n//i not in num_list:
                num_list.append(n//i)
    answer = sum(num_list)
    return answer