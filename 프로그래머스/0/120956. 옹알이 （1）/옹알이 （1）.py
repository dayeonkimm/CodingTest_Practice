def solution(babbling):
    bab_ls = ["aya","ye","woo","ma"]
    bab_dict = {"aya":" ","ye":" ","woo":" ","ma":" "}
    answer = 0
    for i in babbling:
        for j in bab_ls:
            if j in i:
                i = i.replace(j,bab_dict[j])
        i = " ".join(i.split())
        if i == "":
            answer += 1
    return answer