def solution(a, b):
    week = ["THU","FRI","SAT","SUN","MON","TUE","WED"]
    days = {1:31,2:29,3:31,4:30,5:31,6:30,7:31,8:31,9:30,10:31,11:30,12:31}
    answer = 0
    if a != 1:
        for i in range(1,a):
            answer += days[i]%7
    answer += b%7
    return week[answer%7]