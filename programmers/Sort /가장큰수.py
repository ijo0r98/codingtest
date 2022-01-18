# 고득점 kit > 정렬 > 가장 큰 수(L2)

# 1
def solution(numbers):
    answer = ''

    str_array = sorted(list(map(str, numbers))) # 숫자 -> 문자열
    str_array.sort(key=lambda x: x*3, reverse=True)

    answer = ''.join(str_array)

    return answer if int(answer) != 0 else "0"


# 2
def solution(numbers):
    numbers = list(map(str, numbers))
    numbers.sort(key=lambda x: x*3, reverse=True)
    return str(int(''.join(numbers)))


# 3
import functools

def comparator(a,b):
    t1 = a + b
    t2 = b + a
    return (int(t1) > int(t2)) - (int(t1) < int(t2)) 
    # t1 > t2 : 1 - 0 = 1 (t1이 더 클때)
    # t2 > t1 : 0 - 1 = -1 (t2가 더 클때)
    # t1 == t2 : 0 - 0 = 0 (두 값이 같을 때)

def solution(numbers):
    n = [str(x) for x in numbers] # 숫자 문자열로 변환
    n = sorted(n, key=functools.cmp_to_key(comparator), reverse=True) # 정렬함수comparator 기준 정렬

    answer = str(int(''.join(n)))
    return answer

print(solution([6, 10, 2])) # "6210"
print(solution([3, 30, 34, 5, 9])) # "9534330"
print(solution([0, 0, 0])) # "0"
