def solution(myString, pat):
    reString = myString[::-1]
    repat = pat[::-1]
    indexx = reString.index(repat)
    return reString[indexx:][::-1]