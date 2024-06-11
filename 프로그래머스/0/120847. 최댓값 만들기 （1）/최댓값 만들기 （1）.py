def solution(numbers):
    max1 = max(numbers)
    numbers.pop(numbers.index(max1))
    max2 = max(numbers)
    return max1*max2