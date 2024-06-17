def solution(num, k):
    count = 0
    for i in str(num):
        count +=1 
        if int(i) == k:
            return count
    return -1