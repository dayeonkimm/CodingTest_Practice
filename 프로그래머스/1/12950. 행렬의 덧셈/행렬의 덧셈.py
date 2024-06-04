def solution(arr1, arr2):
    answer = []
    for a,b in zip(arr1,arr2):
        row = []
        for j in range(len(a)):
            s = a[j]+b[j]
            row.append(s)
        answer.append(row)

    return answer


def solution(A,B):
    answer = [[c + d for c, d in zip(a,b)] for a, b in zip(A,B)]
    return answer
