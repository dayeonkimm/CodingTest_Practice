def solution(cards1, cards2, goal):
    for word in goal:
        if len(cards1) > 0 and word == cards1[0]:
            del cards1[0]
        elif len(cards2) > 0 and word == cards2[0]:
            del cards2[0]
        else:
            return "No"
    return "Yes"