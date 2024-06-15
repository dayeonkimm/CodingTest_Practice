def solution(s, n):
    upper = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
    lower = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    answer = ''
    for i in range(len(s)):
        if s[i] == " ":
            answer += " "
        if s[i] in upper:
            num = upper.index(s[i])
            if num+n < len(upper):
                answer += upper[num+n]
            else:
                answer += upper[(num+n)%len(lower)]
        if s[i] in lower:
            num = lower.index(s[i])
            if num+n < len(lower):
                answer += lower[num+n]
            else:
                answer += lower[(num+n)%len(lower)]
    return answer