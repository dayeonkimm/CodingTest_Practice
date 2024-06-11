def solution(strings, n): 
    
    for i in range(len(strings)):
        strings[i] = strings[i][n]+strings[i]
    
    strings.sort()
    
    for j in range(len(strings)):
        strings[j] = strings[j][1:]
        
    return strings

