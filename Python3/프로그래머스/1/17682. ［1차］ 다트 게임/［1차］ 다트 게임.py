def solution(dartResult):
    br=0
    li=[]
    ans=[0]*3
    for i in range(len(dartResult)):
        if len(li)==2:
            li.append(list(dartResult[br:]))
            break
        if dartResult[i] in ["S","D","T"]:
            if dartResult[i+1] in ["*","#"]:
                li.append(list(dartResult[br:i+2]))
                br=i+2
            else:
                li.append(list(dartResult[br:i+1]))
                br=i+1 
    for i in range(len(li)):
        for j in range(len(li[i])):
            if li[i][j].isdecimal():
                if li[i][j+1].isdecimal():
                    ans[i]+=10
                else:
                    ans[i]+=int(li[i][j])
            if li[i][j]=="S":
                pass
            if li[i][j]=="D":
                ans[i]**=2
            if li[i][j]=="T":
                ans[i]**=3
            if li[i][j]=="*":
                ans[i]*=2
                if i!=0:
                    ans[i-1]*=2
            if li[i][j]=="#":
                ans[i]*=-1
    return sum(ans)