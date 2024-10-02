def solution(strArr):
    lenArr = [0]*31
    for i in strArr:
        lenArr[len(i)] += 1
    return max(lenArr)

