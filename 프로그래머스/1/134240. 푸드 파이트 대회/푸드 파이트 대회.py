def solution(food):
    answer = ''
    for i in range(len(food)):
        if i == 0:
            pass
        else:
            answer += (food[i]//2)*str(i)
    answer = answer + "0" + answer[::-1]
    return answer