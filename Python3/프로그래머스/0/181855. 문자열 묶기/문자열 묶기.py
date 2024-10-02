def solution(strArr):
    lenArr = []
    answer = 0
    for i in strArr:
        lenArr.append(len(i))
    for j in range(1,31):
        if lenArr.count(j) > answer:
            answer = lenArr.count(j)
    return answer