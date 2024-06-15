def solution(n, arr1, arr2):
    new_arr1 = []
    new_arr2 = []
    for i in arr1:
        new = ""
        while i>=2:
            new += str(i%2)
            i=i//2
        new += str(i)
        new_arr1.append(new[::-1])
        
    for j in arr2:
        new2 = ""
        while j>=2:
            new2 += str(j%2)
            j=j//2
        new2 += str(j)
        new_arr2.append(new2[::-1])
    
    
    origin = []
    for i in range(n):
        origin.append((int(new_arr1[i])+int(new_arr2[i])))
    
    print(origin)
    
    answer = []
            
    for i in origin:
        answer_part = ""
        if len(str(i))<n:
            answer_part += " " * (n-len(str(i)))
        for j in str(i):
            if int(j) == 0:
                answer_part += " "
            else:
                answer_part += "#"
        answer.append(answer_part)
    
    return answer