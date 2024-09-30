def solution(wallet, bill):
    wallet.sort(reverse=True)
    bill.sort(reverse=True)
    answer = 0
    while bill[0]>wallet[0]:
        bill[0]=bill[0]//2
        answer+=1
        bill.sort(reverse=True)
    while bill[1]>wallet[1]:
        bill[0]=bill[0]//2
        answer+=1
        bill.sort(reverse=True)
    return answer