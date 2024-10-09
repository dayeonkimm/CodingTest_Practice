def solution(my_string, overwrite_string, s):
    li=list(my_string)
    li[s:s+len(overwrite_string)]=list(overwrite_string)
    return "".join(li)