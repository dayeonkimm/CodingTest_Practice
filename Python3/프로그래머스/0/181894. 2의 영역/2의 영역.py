def solution(arr):
    if 2 not in arr:
        return [-1]
    if arr.count(2) == 1:
        return [2]
    else:
        a = arr.index(2)
        rearr = arr[::-1]
        b = rearr.index(2)
        return arr[a:len(arr)-b]