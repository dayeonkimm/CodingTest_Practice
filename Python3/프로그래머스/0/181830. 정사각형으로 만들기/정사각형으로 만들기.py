def solution(arr):
    a=len(arr)
    b=len(arr[0])
    if a>b:
        for i in arr:
            for j in range(a-b):
                i.append(0)
    else:
        for k in range(b-a):
            arr.append([0]*b)
    return arr