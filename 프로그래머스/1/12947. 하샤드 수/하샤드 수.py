def solution(x):
    ls = list(str(x))
    y = 0
    for num in ls:
        y += int(num)
    if x % y == 0:
        answer = True
    else:
        answer = False
    return answer



# return n%sum(int(x) for x in str(n)) == 0
