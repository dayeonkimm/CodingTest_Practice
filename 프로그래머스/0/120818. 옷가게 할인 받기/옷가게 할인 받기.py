import math

def solution(price):
    if 100000 <= price < 300000:
        answer = price * 0.95
    elif 300000 <= price < 500000:
        answer = price * 0.9
    elif price >= 500000:
        answer = price * 0.8
    else:
        answer = price
    return math.floor(answer)