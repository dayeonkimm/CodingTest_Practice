def solution(s):
    answer = 0
    first = ""
    first_count = 0
    not_count = 0
    for i in range(len(s)):
        if first == "":
            first = s[i]
            
        if s[i] == first:
            first_count += 1
        else:
            not_count += 1
            
        if first_count == not_count:
            answer += 1
            first = ""
            first_count=0
            not_count=0
        elif i == len(s)-1:
            answer += 1
            
    return answer