def solution(arr, queries):
    answer = []
    for query in queries:
        for i in range(query[0],query[1]+1):
            if query[2] == 0:
                pass
            if i%query[2]==0:
                arr[i] += 1
    return arr