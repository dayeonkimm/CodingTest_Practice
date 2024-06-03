def solution(arr):
    min_num = min(arr)
    arr.remove(min_num)
    if arr == []:
        arr = [-1]
    return arr