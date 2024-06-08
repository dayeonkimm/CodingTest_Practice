def solution(sides):
    n = sides.index(max(sides))
    if sides.pop(n) < sum(sides):
        return 1
    else:
        return 2