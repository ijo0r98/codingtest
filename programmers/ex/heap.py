import heapq

heap_items = [1,3,5,7,9]

max_heap = []
for item in heap_items:
  heapq.heappush(max_heap, (-item, item)) # 튜플로 변환하여 삽입

print(max_heap)

new_item = 11
heapq.heappush(max_heap, (-new_item, new_item))
print(max_heap)

max_item = heapq.heappop(max_heap)[1]
print(max_item)
print(max_heap)