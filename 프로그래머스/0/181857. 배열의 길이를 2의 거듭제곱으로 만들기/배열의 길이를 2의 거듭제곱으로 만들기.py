def solution(arr):
    for i in range(10):
        if len(arr) > 2**i:
            ans = ([0]*(2**(i+1)-len(arr)))
            arr = arr + ans
    return arr