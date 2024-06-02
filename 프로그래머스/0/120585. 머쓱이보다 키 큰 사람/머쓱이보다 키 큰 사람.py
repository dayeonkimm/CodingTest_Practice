def solution(array, height):
    answer = []
    for i in array:
        if i > height:
            answer.append(i)
    return len(answer)