# 완전탐색 > 소수 찾기(L2)

# 1
from itertools import permutations

def solution(numbers):
    answer = []

    nums = list(map(int, numbers))
    length = len(nums)

    perms = []
    for i in range(1, length + 1):
        perms.extend(list(permutations(nums, i))) # 순열
    
    num_list = set()
    for p in perms:
        p = tuple(map(str, p)) # 튜플의 숫자 이어서 숫자 생성
        num = int(''.join(p))
        if num > 1:
            num_list.add(num) # 0과 1 제외

    for n in num_list:
        if is_prime_number(n): 
            answer.append(n)

    return len(answer)

def is_prime_number(x):
    for i in range(2, x):
        if x % i == 0:
            return False 
    return True 


# 2
from itertools import permutations

def solution(numbers):
    a = set()

    for i in range(len(numbers)):
        # 순열로 생성한 튜플을 바로 join으로 하나의 문자열로 만든 뒤 map(int, )로 바로 변환
        a |= set(map(int, map("".join, permutations(list(numbers), i + 1)))) 

    a -= set(range(0, 2)) # 0-1 제외

    # 에라토스테네스 체
    for i in range(2, int(max(a) ** 0.5) + 1):
        a -= set(range(i * 2, max(a) + 1, i))

    return len(a)


# 3
primeSet = set()

def isPrime(number): # 소수 판별 메서드
    if number in (0, 1):
        return False
    for i in range(2, number):
        if number % i == 0:
            return False

    return True

def makeCombinations(str1, str2):
    if str1 != "":
        if isPrime(int(str1)):
            primeSet.add(int(str1))

    for i in range(len(str2)):
        makeCombinations(str1 + str2[i], str2[:i] + str2[i + 1:])

def solution(numbers):
    makeCombinations("", numbers)
    answer = len(primeSet)

    return answer



print('answer: ', solution("17")) # 3
print('answer: ', solution("011")) # 2