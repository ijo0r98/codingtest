# collections.defaultdict
# 키가 없을 경우 미리 지정해놓은 초기값 반환
# httpsd://docs.python.org/3.3/library/collections.html#collections.defaultdict

from collections import defaultdict

# ## defaultdict(default_factory, key=value, ...)
# dict = defaultdict(a=1, b=2)
# print(dict) # defaultdict(None, {'a': 1, 'b': 2})
# print(dict['c']) # KeyError: 'c'

# def default_factory():
#     return 'null'
# dict = defaultdict(default_factory, a=1, b=2)
# print(dict) # defaultdict(<function default_factory at 0x1008f8040>, {'a': 1, 'b': 2})
# print(dict['c']) # null

# # default_factory -> 메서드 형태로 주어짐
# ex_list = defaultdict(list, a=[1,2], b=[3,4])
# print(ex_list) # defaultdict(<class 'list'>, {'a': [1, 2], 'b': [3, 4]})
# print(ex_list['c']) # []

# ex_set = defaultdict(set, a={1,2}, b={3,4})
# print(ex_set) # defaultdict(<class 'set'>, {'a': {1, 2}, 'b': {3, 4}})
# print(ex_set['c']) # set()

# ex_int = defaultdict(int, a=1, b=2)
# print(ex_int) # defaultdict(<class 'int'>, {'a': 1, 'b': 2})
# print(ex_int['c']) # 0


list_ = ['a', 'b', 'c', 'b', 'a', 'b', 'c']
dict_ = {}
for k in list_:
    dict_.setdefault(k, 0) # 기본 딕셔너리(d)의 초기값 지정
    dict_[k] += 1
    print(list(dict_.items()))