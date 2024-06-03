def solution(numbers):
    ls = []
    for i in range(1,10):
        if i not in numbers:
            ls.append(i)
    answer = sum(ls)
    return answer