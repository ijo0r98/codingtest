import sys
input = sys.stdin.readline
from collections import deque


M, N, K = map(int, input().split())
secret = deque(list(map(int, input().split())))
user = deque(list(map(int, input().split())))
queue = deque()

while user:
    queue.append(user.popleft())
    if len(queue) > M: queue.popleft()
    if queue == secret: break
print('secret' if secret == queue else 'normal')