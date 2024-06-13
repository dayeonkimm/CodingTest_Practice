def solution(numbers, direction):
    if direction == "right":
        numbers.insert(0, numbers.pop(-1))
    if direction == "left":
        numbers.insert(len(numbers), numbers.pop(0))
    return numbers