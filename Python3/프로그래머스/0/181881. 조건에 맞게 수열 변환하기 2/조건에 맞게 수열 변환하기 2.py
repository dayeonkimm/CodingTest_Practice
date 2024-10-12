def solution(arr):
    answer = 0
    q=1
    while q>0:
        q=0
        for i in range(len(arr)):
            if arr[i]>=50 and arr[i]%2==0:
                new=arr[i]//2
                q+=1
                arr[i]=new
            elif arr[i]<50 and arr[i]%2!=0:
                new=arr[i]*2+1
                q+=1
                arr[i]=new
        answer+=1
    return answer-1