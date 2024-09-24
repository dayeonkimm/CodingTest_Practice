def solution(array, n):
    answer = 0
    array.append(n)
    array.sort()
    ind=array.index(n)
    if ind==0:
        return array[1]
    elif ind==len(array)-1:
        return array[len(array)-2]
    else:
        small=array[ind-1]
        large=array[ind+1]
        a = n-small
        b = large-n
        if a<=b:
            return small
        else:
            return large