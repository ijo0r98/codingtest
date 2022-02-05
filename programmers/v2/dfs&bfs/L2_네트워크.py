# 깊이/너비 우선 탐색(DFS/BFS) > 네트워크

# 1 왜 안되는지 모르겠음..
def dfs(graph):
    stack = [0]
    visited = []

    while stack:
        node = stack.pop()
        if node not in visited:
            stack.extend(graph[node])
            visited.append(node)
    
    # print(visited)
    return visited
    


def solution(n, computers):
    answer = 0
    try: 
        graph = [list() for i in range(n+1)]
        nodes = [i for i in range(n)]

        for i in range(n-1):
            for j in range(i+1, n):
                if (computers[i][j] == 1):
                    graph[i].append(j)
                    graph[j].append(i)

        total_visited = []

        while True:
            if len(total_visited) == n:
                break
            total_visited.extend(dfs(graph))
            total_visited.sort()
            graph = graph[total_visited[-1]:]    
            answer += 1

        return answer
    except:
        print(i, j, computers[i][j])
  
# 다른 사람 코드 (재귀 안씀)
def solution(n, computers):
    answer = 0
    bfs = []
    visited = [0]*n

    while 0 in visited:
        x = visited.index(0)
        bfs.append(x)
        visited[x] = 1
        
        while bfs:
            node = bfs.pop(0)
            visited[node] = 1
            for i in range(n):
                if visited[i] == 0 and computers[node][i] == 1:
                    bfs.append(i)
                    visited[i] = 1
        answer += 1
    return answer      
        
# 내 코드
# dfs
def dfs(computers, visited, start):
    visited[start] = True
    for node in computers:
        if node not in visited:
            dfs(computers, visited, node)
    return visited       

def solution(n, computers):
    answer = 0
     
    visited = [False for i in range(n)]
    for computer in computers:
        if visited[computer] == False:
            dfs(computers, visited, computer)
            
     
    for i in range(n-1):
        for j in range(i+1, n):
            if (computers[i][j] == 1):
                graph[i].append(j)
                graph[j].append(i)
                
    

    return answer
    
        
# 다른 사람 코드
def solution(n, computers):
    answer = 0
    visited = [False for i in range(n)]
    for com in range(n):
        if visited[com] == False:
            DFS(n, computers, com, visited)
            answer += 1 
    return answer

def DFS(n, computers, com, visited):
    visited[com] = True
    for connect in range(n):
        if connect != com and computers[com][connect] == 1:
            if visited[connect] == False:
                DFS(n, computers, connect, visited)
