def solution(my_string, is_suffix):
    if my_string[len(my_string)-len(is_suffix):len(my_string)] == is_suffix:
        return 1
    else:
        return 0