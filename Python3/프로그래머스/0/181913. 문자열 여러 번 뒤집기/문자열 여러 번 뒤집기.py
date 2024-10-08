def solution(my_string, queries):
    my_list=list(my_string)
    for a,b in queries:
        new=my_list[a:b+1][::-1]
        my_list[a:b+1]=new
    return "".join(my_list)