def solution(before, after):
    before_ls = list(before)
    for i in after:
        if i in before_ls: 
            before_ls.pop(before_ls.index(i))
    if len(before_ls) == 0:
        return 1
    else:
        return 0