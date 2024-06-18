def solution(nums):
    num = []
    for i in nums:
        if i not in num:
            num.append(i)
    if len(nums)/2 >= len(num):
        return len(num)
    else:
        return len(nums)/2