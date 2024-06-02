def solution(n):
    n = str(n)
    num_list = list(n)
    new_list = []
    for i in num_list:
        k = 0
        if len(new_list) == 0:
            new_list.append(i)
        else:
            for j in new_list:
                if i <= new_list[-1]:
                    new_list.append(i)
                    break
                elif i >= j:
                    new_list.insert(k,i)
                    break
                else:
                    k += 1
    answer = int("".join(new_list))
    return answer



def solution_2(n):
    num_list = list(str(n))
    num_list.sort(reverse = True)
    answer = int("".join(num_list))
    return answer
