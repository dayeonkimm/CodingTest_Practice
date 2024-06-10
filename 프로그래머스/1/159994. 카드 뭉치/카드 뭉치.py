def solution(cards1, cards2, goal):
    i = 0
    j = 0
    for word in goal:
        if word == cards1[i]:
            i += 1
            if i == len(cards1):
                i =0
        elif word == cards2[j]:
            j += 1
            if j == len(cards2):
                j =0
        else:
            return "No"
    return "Yes"