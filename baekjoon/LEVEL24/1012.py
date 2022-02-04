# BFS/DFS > 유기농 배추

def dfs_feild(graph):
    visited = [graph[0]]
    stack = [graph[0]]
    while stack:
        node = stack.pop()
        for g in graph:
            if ((g[0]==node[0]) and (abs(g[1]-node[1])==1)) or ((g[1]==node[1]) and (abs(g[0]-node[0])==1)):
                if g not in visited:
                    visited.append(g)
                    stack.append(g)
    return visited

def solution(graph, w, h, k):
    # total_visited = []
    cnt = 0
    while graph:
        tmp = dfs_feild(graph)
        graph = list(set(graph) - set(tmp)) # 남은 아파트들
        cnt += 1
       
    return cnt
    
    
# main
test = int(input())
answer = []
for i in range(test):
    graph = []
    m, n, k = map(int, input().split())
    for i in range(k):
        i, j = map(int, input().split())
        graph.append((i, j))
        graph.sort(key=lambda x:(x[0], x[1]))
    answer.append(solution(graph, m, n, k))
    
for a in answer:
    print(a)