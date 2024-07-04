def solution(numbers, hand):
    answer = ''
    
    numbers_dic = {1:[0,3], 
                   2:[1,3], 
                   3:[2,3], 
                   4:[0,2], 
                   5:[1,2], 
                   6:[2,2], 
                   7:[0,1], 
                   8:[1,1], 
                   9:[2,1], 
                   0:[1,0], 
                   "*":[0,0], 
                   "#":[2,0]}
    
    left = "*"
    right = "#"
    
    for i in numbers:
        if i in [1,4,7]:
            answer += "L"
            left = i
        elif i in [3,6,9]:
            answer += "R"
            right = i
        else:
            left_d = max(numbers_dic[i][0],numbers_dic[left][0])-min(numbers_dic[i][0],numbers_dic[left][0])+max(numbers_dic[i][1],numbers_dic[left][1])-min(numbers_dic[i][1],numbers_dic[left][1])
            right_d = max(numbers_dic[i][0],numbers_dic[right][0])-min(numbers_dic[i][0],numbers_dic[right][0])+max(numbers_dic[i][1],numbers_dic[right][1])-min(numbers_dic[i][1],numbers_dic[right][1])
            if left_d < right_d:
                answer += "L"
                left = i
            elif left_d > right_d:
                answer += "R"
                right = i
            else:
                if hand == "left":
                    answer += "L"
                    left = i
                else:
                    answer += "R"
                    right = i
            
    
    
    
    return answer