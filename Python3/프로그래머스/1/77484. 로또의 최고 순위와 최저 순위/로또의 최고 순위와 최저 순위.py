def solution(lottos, win_nums):
    ranks = [6,6,5,4,3,2,1]
    right = 0
    zeros = lottos.count(0)
    for i in lottos:
        if i in win_nums:
            right += 1
    return [ranks[right+zeros],ranks[right]]