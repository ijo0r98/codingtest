# DFS/BFS > 바이러스

import collections

n = int(input())
m = int(input())
graph = collections.defaultdict(list)

for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
    # graph[a].sort()
    # graph[b].sort()

def bfs(graph, start):
    visited = []
    queue = [start]
    
    while queue:
        node = queue.pop()
        if node not in visited:
            visited.append(node)
            queue.extend(graph[node])
            
    return visited
        

print(len(bfs(graph, 1))-1)


    