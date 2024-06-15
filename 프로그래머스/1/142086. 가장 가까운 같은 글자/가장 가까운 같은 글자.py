def solution(s):
    answer = [-1]
    for i in range(1,len(s)):
        new_s = s[:i][::-1]
        for j in range(len(new_s)):
            count = 0
            if new_s[j] == s[i]:
                answer.append(j+1)
                count += 1
                break
        if count==0:
            answer.append(-1)
    return answer