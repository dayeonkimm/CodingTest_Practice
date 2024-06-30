def solution(n, lost, reserve):
    # 여분의 체육복이 있는 학생이 체육복을 잃어버린 경우 처리
    reserve_set = set(reserve) - set(lost)
    lost_set = set(lost) - set(reserve)

    # 여분의 체육복을 가진 학생이 체육복을 빌려주는 과정
    for i in sorted(reserve_set):
        if i - 1 in lost_set:
            lost_set.remove(i - 1)
        elif i + 1 in lost_set:
            lost_set.remove(i + 1)

    # 체육 수업에 참가할 수 있는 학생 수 계산
    return n - len(lost_set)