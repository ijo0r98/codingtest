# DFS/BFS > DFS와 BFS

import collections

n, m, v = map(int, input().split())
graph = collections.defaultdict(list)

for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
    graph[a].sort()
    graph[b].sort()
    
    
# dfs 재귀
def dfs_recursive(graph, start, visited):
    visited.append(start)
    for node in graph[start]:
        if node not in visited:
            dfs_recursive(graph, node, visited)

    return visited

# dfs
def dfs(graph, start):
    visited = []
    stack = [start]
    while stack:
        n = stack.pop()
        if n not in visited:
            visited.append(n)
            stack.extend(graph[n])
    return visited

# bfs
def bfs(graph, start):
    visited = []
    queue = [start]
    # queue.append(start)
    while queue:
        node = queue.pop(0)
        if node not in visited:
            visited.append(node)
            queue.extend(graph[node])
    return visited


for node in dfs_recursive(graph, v, []): # dfs(graph, v)
    print(node, end=' ')
print()
for node in bfs(graph, v):
    print(node, end=' ')



