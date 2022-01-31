# 고득점 kit > stack&queue > 다리를 지나는 트럭(L2)

# 다리 길이 bridge_length (int)
# 한번에 다리에 올라갈 수 있는 최대 무게 weight (int)
# 지나가려는 트럭들의 무게 truck_weights (list)

# 1-1
from collections import deque

def solution(bridge_length, weight, truck_weights):
    on_bridge = [] # 다리 위
    sum_weight = 0
    time = 0

    while truck_weights:
        time += 1

        while on_bridge and on_bridge[0][0] <= time: # 건너고 있는 트럭이 있고, 가장 앞서있는 트럭이 다 건넜을 때
            print(time,' ', on_bridge)
            _, w = on_bridge.pop(0) # 맨 앞선 트럭 제거
            sum_weight -= w # 전체 무게에서 제거

        if sum_weight + truck_weights[0] <= weight: # 무게가 남을 때
            truck = truck_weights.pop(0) # 가장 먼저 있는 대기중인 트럭
            on_bridge.append((bridge_length + time, truck)) # tuple(추가된 트럭이 다리를 건너는데 걸리는 시간, 트럭 무게)
            sum_weight += truck # 다리 위 트럭들의 무게 합

    return on_bridge[-1][0] # 마지막 트럭의 시간

# 1-2
def solution(bridge_length, weight, truck_weights):
    truck_weights = deque(truck_weights)
    on_bridge = deque() # 다리 위
    sum_weight = 0
    time = 0

    while truck_weights:
        time += 1

        while on_bridge and on_bridge[0][0] <= time: # 건너고 있는 트럭이 있고, 가장 앞서있는 트럭이 다 건넜을 때
            print(time,' ', on_bridge)
            _, w = on_bridge.popleft() # 맨 앞선 트럭 제거
            sum_weight -= w # 전체 무게에서 제거

        if sum_weight + truck_weights[0] <= weight: # 무게가 남을 때
            truck = truck_weights.popleft() # 가장 먼저 있는 대기중인 트럭
            on_bridge.append((bridge_length + time, truck)) # tuple(추가된 트럭이 다리를 건너는데 걸리는 시간, 트럭 무게)
            sum_weight += truck # 다리 위 트럭들의 무게 합

    return on_bridge[-1][0] # 마지막 트럭의 시간


# 2
import collections

DUMMY_TRUCK = 0

class Bridge(object):

    def __init__(self, length, weight):
        self._max_length = length
        self._max_weight = weight
        self._queue = collections.deque()
        self._current_weight = 0

    def push(self, truck):
        next_weight = self._current_weight + truck
        if next_weight <= self._max_weight and len(self._queue) < self._max_length:
            self._queue.append(truck)
            self._current_weight = next_weight
            return True
        else:
            return False

    def pop(self):
        item = self._queue.popleft()
        self._current_weight -= item
        return item

    def __len__(self):
        return len(self._queue)

    def __repr__(self):
        return 'Bridge({}/{} : [{}])'.format(self._current_weight, self._max_weight, list(self._queue))


def solution(bridge_length, weight, truck_weights):
    bridge = Bridge(bridge_length, weight)
    trucks = collections.deque(w for w in truck_weights)

    for _ in range(bridge_length):
        bridge.push(DUMMY_TRUCK)

    count = 0
    while trucks:
        bridge.pop()

        if bridge.push(trucks[0]):
            trucks.popleft()
        else:
            bridge.push(DUMMY_TRUCK)

        count += 1

    while bridge:
        bridge.pop()
        count += 1

    return count

def main():
    print(solution(2, 10, [7, 4, 5, 6]), 8)
    print(solution(100, 100, [10]), 101)
    print(solution(100, 100, [10, 10, 10, 10, 10, 10, 10, 10, 10, 10]), 110)


if __name__ == '__main__':
    main()


# 3
from collections import deque

def solution(bridge_length, weight, truck_weights):
    bridge = deque(0 for _ in range(bridge_length))
    total_weight = 0
    step = 0
    truck_weights.reverse()

    while truck_weights:
        total_weight -= bridge.popleft()
        if total_weight + truck_weights[-1] > weight:
            bridge.append(0)
        else:
            truck = truck_weights.pop()
            bridge.append(truck)
            total_weight += truck
        step += 1

    step += bridge_length

    return step



#####
b1, w1, t1 = 2, 10, [7,4,5,6]
print(solution(b1, w1, t1)) # 8

b2, w2, t2 = 100, 100, [10]
# print(solution(b2, w2, t2)) # 101

b3, w3, t3 = 100, 100, [10,10,10,10,10,10,10,10,10,10]
# print(solution(b3, w3, t3)) # 110