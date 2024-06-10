def solution(my_string, is_prefix):
    if my_string[0:len(is_prefix)] == is_prefix:
        return 1
    else:
        return 0