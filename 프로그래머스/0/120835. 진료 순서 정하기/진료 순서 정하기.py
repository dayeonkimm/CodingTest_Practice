def solution(emergency):
    s_emergency = sorted(emergency,reverse=True)
    answer = []
    for i in emergency:
        answer.append(s_emergency.index(i)+1)
    return answer