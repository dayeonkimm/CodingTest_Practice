def solution(numbers, k):
    numbers = numbers*((2*k)//len(numbers)+1)
    return numbers[2*(k-1)]
        