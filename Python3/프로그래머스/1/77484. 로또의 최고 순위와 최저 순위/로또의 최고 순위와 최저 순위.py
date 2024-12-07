def solution(lottos, win_nums):
    answer = []
    right = 0
    zeros = lottos.count(0)
    for i in lottos:
        if i in win_nums:
            right += 1
    if right >=2:
        answer.append(7-right-zeros)
        answer.append(7-right)
    elif right == 1:
        answer.append(6-zeros)
        answer.append(6)
    elif right == 0 and zeros == 0:
        return [6,6]
    else:
        answer.append(7-zeros)
        answer.append(6)
            
    return answer