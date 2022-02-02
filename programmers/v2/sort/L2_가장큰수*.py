# 정렬 > 가장 큰 수

def solution(numbers):
    numbers = [str(n) for n in numbers]
    # numbers = sorted(numbers, key=lambda x: (x[0], len(x), reverse=True)
    # numbers.sort(key=(numbers, len(numbers)), reverse=True)
    numbers.sort(key=lambda x: x*3, reverse=True)
    return ''.join(numbers)