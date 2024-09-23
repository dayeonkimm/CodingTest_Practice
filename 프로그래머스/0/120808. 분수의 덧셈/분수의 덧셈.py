def solution(numer1, denom1, numer2, denom2):
    answer = []
    x=denom1
    y=denom2
    while(y):
        x,y=y,x%y
    z=x
    denom=int(denom1*denom2/z)
    nnumer1=numer1*(denom/denom1)
    nnumer2=numer2*(denom/denom2)
    numer=int(nnumer1+nnumer2)
    
    x1=numer
    y1=denom
    while(y1):
        x1,y1=y1,x1%y1
    z1=x1
    
    if z1 == 1:
        answer.append(numer)
        answer.append(denom)
    else:
        answer.append(int(numer/z1))
        answer.append(int(denom/z1))
    return answer