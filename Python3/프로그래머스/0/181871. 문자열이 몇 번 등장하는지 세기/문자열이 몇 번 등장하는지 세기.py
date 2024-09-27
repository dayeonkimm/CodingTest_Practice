def solution(myString, pat):
    count = 0
    while pat in myString:
        count += 1
        new = myString.index(pat)
        myString = myString[new+1:]
    return count