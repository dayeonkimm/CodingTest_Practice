def solution(arr):
    for i in range(0,len(arr)):
        for j in range(0,len(arr[0])):
            if arr[i][j] != arr[j][i]:
                return 0
    return 1