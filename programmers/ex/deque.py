# collections.deque (double ended queue)
# 양방향 데이터 처리가 가능한 큐 자료형
# https://docs.python.org/3/library/collections.html#collections.deque

from collections import deque

list = ['a', 'b', 'c']
Q = deque(['A', 'B', 'C'])

# append
list.append('d') # ['a', 'b', 'c', 'd']
Q.append('D') # ['A', 'B', 'C', 'D']

# appendleft
Q.appendleft('X') # ['X', 'A', 'B', 'C', 'D']

# extend(iterable)
list.extend('ef')  # ['a', 'b', 'c', 'd', 'e', 'f']
Q.extend('EF') # ['X', 'A', 'B', 'C', 'D', 'E', 'F']

# extendlieft(iterable)
Q.extendleft('YZ') # ['Z', 'Y', 'X', 'A', 'B', 'C', 'D', 'E', 'F']

# pop
lst = ['a', 'b', 'c']
while True:
    try:
        print(lst.pop(), end=' ') # c b a
    except IndexError:
        break

q = deque(['A', 'B', 'C'])
while True:
    try:
        print(q.pop(), end=' ') # C B A
    except IndexError:
        break


# popleft()
q = deque(['A', 'B', 'C'])
while True:
    try:
        print(q.popleft(), end=' ') # A B C
    except IndexError:
        break


# rotate(n) n만큼 회전, 음수이면 왼쪽, 양수이면 오른쪽
deq = deque(['a', 'b', 'c', 'd', 'e'])
deq.rotate(1) # e a b c d

deq2 = deque(['a', 'b', 'c', 'd', 'e'])
deq2.rotate(2) # d e a b c

deq3 = deque(['a', 'b', 'c', 'd', 'e']) 
deq3.rotate(-1) # b c d e a

deq4 = deque(['a', 'b', 'c', 'd', 'e']) 
deq4.rotate(-2) # c d e a b 


def print_ex(list, Q):
    print(list)
    print(Q)

# print_ex(list, Q)