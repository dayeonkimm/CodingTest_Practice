def solution(myStr):
    myStr = myStr.replace("a"," ")
    myStr = myStr.replace("b"," ")
    myStr = myStr.replace("c"," ")
    answer = list(myStr.split())
    
    if answer == []:
        answer.append("EMPTY")
        
    return answer