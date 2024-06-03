def solution(price, money, count):
    amount = 0
    for i in range(1,count+1):    
        amount += price*i
    answer = amount - money
    if answer < 0:
        answer = 0
    return answer