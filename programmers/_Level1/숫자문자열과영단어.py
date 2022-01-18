# 코딩테스트 연습 >2021 카카오 채용연계형 인턴십 > 숫자 문자열과 영단어


# 내 풀이
def solution(s):
    answer = ''
    tmp = ''

    nums = {'zero': '0', 'one': '1', 'two': '2', 'three': '3', 'four': '4', 'five': '5', 'six': '6', 'seven': '7', 'eight': '8', 'nine': '9'}
    
    s_list = list(s)
    
    for i in s_list:
        if i.isdigit():
            answer += i
        else:
            tmp += i
            if tmp in list(nums.keys()):
                answer += nums[tmp]
                tmp = ''

    return int(answer)


# 다른 사람 풀이 1
num_dic = {"zero": "0", "one": "1", "two": "2", "three": "3", "four": "4", "five": "5", "six": "6", "seven": "7", "eight": "8", "nine": "9"}

def solution(s):
    answer = s
    for key, value in num_dic.items():
        answer = answer.replace(key, value)
    return int(answer)


# 다른 사람 풀이 2
def solution(s):
    words = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

    for i in range(len(words)):
        s = s.replace(words[i], str(i))

    return int(s)


print('answer: ', solution("one4seveneight")) # 1478
print('answer: ', solution("23four5six7")) # 234567
print('answer: ', solution("2three45sixseven")) # 234567
print('answer: ', solution("123")) # 123


