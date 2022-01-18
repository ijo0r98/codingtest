# collections.Counter
# 컨테이너에 동일한 자료가 몇개인지 파익하여 dict 형태처럼 반환되는 객체

from collections import Counter

# lst = ['aa', 'cc', 'dd', 'aa', 'bb', 'ee']
# print(Counter(lst)) # Counter({'aa': 2, 'cc': 1, 'dd': 1, 'bb': 1, 'ee': 1})

# # 값=개수 형태 입력하여 리스트 반환 가능
# counts = Counter(a=2, b=3, c=2)
# print(Counter(counts)) # Counter({'b': 3, 'a': 2, 'c': 2}) *개수가 많은 것부터 반환
# print(sorted(counts.elements())) # ['a', 'a', 'b', 'b', 'b', 'c', 'c']

# # 문자열
# container = Counter()
# container.update("aabcdeffgg")
# print(container) # Counter({'a': 2, 'f': 2, 'g': 2, 'b': 1, 'c': 1, 'd': 1, 'e': 1})

# for k,v in container.items():
#     print(k, ':', v)
# # a : 2
# # b : 1
# # c : 1
# # d : 1
# # e : 1
# # f : 2
# # g : 2

# # update() 값 갱신

# # elements() 입력된 값의 요소에 해당하는 무작위 반환
# counters = Counter("Hello Python")
# print(list(counters.elements())) # ['H', 'e', 'l', 'l', 'o', 'o', ' ', 'P', 'y', 't', 'h', 'n']
# print(sorted(counters.elements())) # [' ', 'H', 'P', 'e', 'h', 'l', 'l', 'n', 'o', 'o', 't', 'y']

# counters = Counter(a=4, b=2, c=0, d=-2)
# print(sorted(counters.elements())) # ['a', 'a', 'a', 'a', 'b', 'b']

# # most_common(n) 빈도수가 높은 순으로 상위 n개 튜플 형태로 반환, n이 없을 시 전체 반환
# counters = Counter('apple, orange, grape') 
# print(counters.most_common()) # [('a', 3), ('p', 3), ('e', 3), (',', 2), (' ', 2), ('r', 2), ('g', 2), ('l', 1), ('o', 1), ('n', 1)]
# print(counters.most_common(3)) # [('a', 3), ('p', 3), ('e', 3)]

# # substract() 차집합과 비슷하게 요소를 뺌, 없을 경우 -1
# c1 = Counter('hello python')
# c2 = Counter('i love python')
# c1.subtract(c2)
# print(c1) # Counter({'h': 1, 'l': 1, 'e': 0, 'o': 0, 'p': 0, 'y': 0, 't': 0, 'n': 0, ' ': -1, 'i': -1, 'v': -1})

# # 산술, 집합 연산 가능

a = Counter(['a', 'b', 'c', 'b', 'd', 'a'])
b = Counter('aaeroplane')

print(a|b)