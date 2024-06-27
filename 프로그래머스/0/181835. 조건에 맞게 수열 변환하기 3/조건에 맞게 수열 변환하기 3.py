def solution(arr, k):
    if k%2 != 0:
        for i in range(len(arr)):
            arr[i] = k*arr[i]
    else:
        for i in range(len(arr)):
            arr[i] = k+arr[i]
    return arr