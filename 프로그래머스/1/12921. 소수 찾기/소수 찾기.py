# def solution(n):
#     sosu = []
#     for i in range(2,n+1):
#         if sosu == []:
#             sosu.append(i)
#         else:
#             count = 0
#             for s in sosu:
#                 if i%s == 0:
#                     break
#                 count += 1
#             if count==len(sosu):
#                 sosu.append(i)
#     return len(sosu)


def solution(n):
    answer = 0
    for i in range(2,n+1):
        sq = int(i**(1/2))+1
        count = 0
        for j in range(2,sq):
            if i%j == 0:
                break
            count +=1
        if count == sq-2:
            answer += 1
    
    return answer 


