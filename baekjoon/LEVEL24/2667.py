# DFS/BFS > 단지번호 붙이기

# dfs 기본
def dfs(graph, node):
    visited = []
    stack = [node]
    while stack:
        node = stack.pop()
        if node not in visited:
            visited.append(node)
            stack.extend(graph[node])
    return visited



def dfs_apt(graph):
    stack = [graph[0]]
    visited = [graph[0]]
    
    while stack:
        node = stack.pop()
        for g in graph:
            if ((g[0] == node[0]) and (abs(g[1]-node[1]) == 1)) or ((g[1] == node[1]) and (abs(g[0]-node[0]) == 1)):
                # i가 같고 j가 1 차이남 -> 가로로 붙어있음, j가 같고 i가 1 차이남 -> 세로로 붙어있음
                if g not in visited:
                    # print(node, g)
                    stack.append(g)
                    visited.append(g)

        # print('dfs: ', node, ' // ', visited)
    return visited
        
n = int(input())
lines = []
apts = []
for i in range(n):
    lines.append((list(input())))
    
cnt = 0 # 총 아파트 수
for i in range(n):
    for j in range(n):
        if lines[i][j] == '1':
            cnt += 1 
            apts.append((i, j))
            
total_visited = [] # 아파트 방문 체크
answer = []
apts.sort(key=lambda x: (x[0], x[1])) # 가로 세로 붙어있는 것을 확인하기위해 정렬

# print(apts)
while True:
    if len(total_visited) == cnt:
        break
    tmp = (dfs_apt(apts)) # 한 단지 내 아파트들
    total_visited.extend(tmp) # 전체 방문여부에 체크
    answer.append(len(tmp)) # 답에 단지 내 아파트 수 추가
    apts = list(set(apts) - set(total_visited)) # 남은 아파트들
    # print('visited: ', tmp)
    # print('apts: ', apts)
    # print("----", answer, '-----')
    
print(len(answer))
answer.sort()
for a in answer:
    print(a)
    