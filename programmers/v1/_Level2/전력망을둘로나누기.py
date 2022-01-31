# 코딩테스트 연습 > 위클리 챌린지 > 전력망을 둘로 나누기

# 하나의 트리형태 -> 2개로 분리

from collections import defaultdict

def solution(n, wires):
    answer = []

    # 완전탐색 
    for i in range(0, len(wires)):
        tmp_wires = wires.copy()
        del tmp_wires[i]
        wires_dict = defaultdict(set)
        for w in tmp_wires:
            wires_dict[w[0]].add(w[1])
            wires_dict[w[1]].add(w[0])
        t1 = bfs(wires_dict, wires[i][0])
        t2 = bfs(wires_dict, wires[i][1])

        # for i in range(1, len(wires)-1):
            # tmp_wires = wires.copy()
            # t1 = search(tmp_wires[:i], n)
            # t2 = search(tmp_wires[i+1:], n)

        answer.append(abs(len(t1) - len(t2)))

    # 가장 작은 차이값 반환
    return min(answer)

def bfs(graph, start_node):
    visit = list()
    queue = list()

    queue.append(start_node)

    while queue:
        node = queue.pop(0)
        if node not in visit:
            visit.append(node)
            queue.extend(graph[node])
 
    return visit


def search_1(wire, n):
    start = wire.pop()
    visit_nodes = [start[0], start[1]]
    
    while wire:
        current = wire.pop()
        if current[0] not in visit_nodes:
            visit_nodes.append(current[0])
        if current[1] not in visit_nodes:
            visit_nodes.append(current[1])

    return visit_nodes


# start 간선을 시작으로 그래프 탐색(DFS)
def search_2(wire, n):
    print(wire)
    start = wire.pop()
    visit_nodes = [start[0], start[1]]
    visited = [[0 for _ in range(n)] for _ in range(n)] # visited = [[0] * len(wire)] * len(wire) 
    for i in range(n): # 자기 자신과의 간선 1
        visited[i][i] = 1
    visited[start[0]-1][start[1]-1] = 1
    
    while wire:
        current = wire.pop()
        
        if visited[current[0]-1][current[1]-1] == 0:
            visited[current[0]-1][current[1]-1] = 1 # 간선 방문 check
            if current[0] not in visit_nodes:
                visit_nodes.append(current[0])
            if current[1] not in visit_nodes:
                visit_nodes.append(current[1])
        else:
            continue

    return visit_nodes


def print2d(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            print(matrix[i][j], end=' ')
        print('\n')



print(solution(9, [[1,3],[2,3],[3,4],[4,5],[4,6],[4,7],[7,8],[7,9]])) # 3
print(solution(4, [[1,2],[2,3],[3,4]])) # 0