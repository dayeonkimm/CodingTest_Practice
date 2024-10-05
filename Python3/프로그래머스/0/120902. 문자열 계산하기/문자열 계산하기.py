def solution(my_string):
    li=list(my_string.split())
    answer = int(li[0])
    for i in range(len(li)):
        if li[i]=="+":
            answer+=int(li[i+1])
        elif li[i]=="-":
            answer-=int(li[i+1])
    return answer