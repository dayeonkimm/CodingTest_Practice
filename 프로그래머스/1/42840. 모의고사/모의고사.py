def solution(answers):
    answer1 = [1,2,3,4,5]
    answer2 = [2,1,2,3,2,4,2,5]
    answer3 = [3,3,1,1,2,2,4,4,5,5]
    
    answer1 = answer1*(len(answers)//5) + answer1[:len(answers)%5]
    answer2 = answer2*(len(answers)//8) + answer2[:len(answers)%8]
    answer3 = answer3*(len(answers)//10) + answer3[:len(answers)%10]

    print(answer1)
    print(answer2)
    print(answer3)
    count1 = 0
    count2 = 0
    count3 = 0
    
    for i in range(len(answers)):
        if answers[i] == answer1[i]:
            count1 += 1
        if answers[i] == answer2[i]:
            count2 += 1
        if answers[i] == answer3[i]:
            count3 += 1
    
    answer = []
    max_answer = max(count1,count2,count3)
    if count1 == max_answer:
        answer.append(1)
    if count2 == max_answer:
        answer.append(2)
    if count3 == max_answer:
        answer.append(3)
    
    return answer