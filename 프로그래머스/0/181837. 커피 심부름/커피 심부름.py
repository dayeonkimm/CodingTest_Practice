def solution(order):
    answer = 0
    for i in order:
        if "latte" in i:
             answer += 5000
        elif "americano" or "anything" in i:
            answer += 4500
    return answer