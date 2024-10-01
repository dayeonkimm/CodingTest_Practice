def solution(arr):
    answer = []
    i = 0
    while i < len(arr):
        if answer == []:
            answer.append(arr[i])
        elif answer[-1] == arr[i]:
            answer.pop()
        elif answer[-1] != arr[i]:
            answer.append(arr[i])
        i += 1
    if answer == []:
        answer.append(-1)
    return answer