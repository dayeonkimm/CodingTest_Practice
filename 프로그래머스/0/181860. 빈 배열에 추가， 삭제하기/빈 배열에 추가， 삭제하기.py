def solution(arr, flag):
    answer = []
    for i in range(len(flag)):
        if flag[i] == True:
            for j in range(arr[i]*2):
                answer.append(arr[i])
        else:
            for k in range(arr[i]):
                answer.pop()
    return answer