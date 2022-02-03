# 탐욕법 > 체육복


# 1
def solution(n, lost, reserve):
    answer = n
    reserve.sort(reverse=True)
    for r in reserve:
        if (r-1 in lost) or (r in lost) or (r+1 in lost):
            lost.pop()
    return n - len(lost)

# 2
def solution(n, lost, reserve):
    answer = n
    reserve.sort()
    lost_ = list(set(lost) - set(reserve))
    reserve = list(set(reserve) - set(lost))
    for r in reserve:
        if (r-1 in lost_) or (r+1 in lost_):
            lost_.pop()
    return n - len(lost_)

# 3
def solution(n, lost, reserve):
    answer = n
    reserve.sort()
    lost_ = list(set(lost) - set(reserve))
    reserve = list(set(reserve) - set(lost))
    for r in reserve:
        if (r-1 in lost_) or (r+1 in lost_):
            lost_ = lost_[1:] # 앞의 학생부터 비교하고 있음으로 앞을 삭제해야함
    return n - len(lost_)