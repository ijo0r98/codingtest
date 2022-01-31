# 2021 KAKAO BLIND RECRUITMENT > 숫자 문자열과 영단어

def solution(s):
    nums = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    
    for i in range(10):
        s = s.replace(nums[i], str(i))
    
    return int(s)