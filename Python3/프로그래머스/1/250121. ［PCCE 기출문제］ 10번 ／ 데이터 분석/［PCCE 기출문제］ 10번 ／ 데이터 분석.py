def solution(data, ext, val_ext, sort_by):
    answer = []
    ext0 = {"code":0,"date":1,"maximum":2,"remain":3}
    ext1 = ext0[ext]
    ext2 = ext0[sort_by]
    for i in data:
        if i[ext1]<val_ext:
            answer.append(i)
    answer = sorted(answer, key=lambda x : x[ext2])
    return answer