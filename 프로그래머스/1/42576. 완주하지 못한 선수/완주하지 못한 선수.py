def solution(participant, completion):
    for n in range(len(participant)-len(completion)):
        completion.append(" ")
    participant.sort(reverse=True)
    completion.sort(reverse=True)
    for i in range(len(participant)):
        if participant[i] != completion[i]:
            return participant[i]