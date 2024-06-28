def solution(ingredient):
    # str_ingre = "".join(map(str,ingredient))
    ls = []
    pattern = [1,2,3,1]
    answer = 0
    for i in ingredient:
        ls.append(i)
        if ls[-4:] == pattern:
            answer += 1
            del ls[-4:]
    return answer

