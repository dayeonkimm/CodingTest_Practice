def solution(arr, queries):
    for i in queries:
        a,b=i
        arr[a],arr[b] = arr[b],arr[a]
    return arr