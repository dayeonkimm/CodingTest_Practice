def solution(arr, queries):
    answer = []
    for query in queries:
        new=[]
        for i in arr[query[0]:query[1]+1]:
            if i>query[2]:
                new.append(i)
            else:
                pass
        if new==[]:
            answer.append(-1)
        else:
            answer.append(min(new))
    return answer