def solution(s, skip, index):
    alpha = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    answer = ''
    
    num = len(skip)
    
    for i in skip:
        alpha.pop(alpha.index(i))
    for str in s:
        new_index = (alpha.index(str) +index)%(26-num)
        new = alpha[new_index]
        
        answer += new
    return answer