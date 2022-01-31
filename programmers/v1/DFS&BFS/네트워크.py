# DFS/BFS > 네트워크(L3) 

# 1

# 2
def solution(n, computers):
    answer = 0

    visited = [False for i in range(n)]

    for com in range(n):
        if visited[com] == False:
            DFS(n, computers, com, visited)
            answer += 1 # 탐색이 끝나면 네트워크 완성
    return answer

def DFS(n, computers, com, visited):
    # 전체 노드 수, 연결 정보, 현재 노드, 방문 노드 정보

    visited[com] = True # 현재 노드 방문 체크

    for connect in range(n):
        if connect != com and computers[com][connect] == 1: # 연결된 컴퓨터
            if visited[connect] == False:
                DFS(n, computers, connect, visited)


# 3
def solution(n, computers):
    temp = []

    for i in range(n):
        temp.append(i) # 전체 노드 정보 저장

    # 하나의 네트워크로 연결될 때 동일한 값으로 바꿔줌
    for i in range(n):
        for j in range(n):
            if computers[i][j]: # 1이면, 연결되어 있으면
                for k in range(n): 
                    # i->j, j->k 이면 i->k 임을 이용
                    if temp[k] == temp[i]:
                        temp[k] = temp[j]

    # 네트워크 하나당 하나의 동일한 값임으로 중복제거하여 개수를 세면 네트워크의 수
    return len(set(temp))



print('answer: ', solution(3, [[1, 1, 0], [1, 1, 0], [0, 0, 1]]))
print('answer: ', solution(3, [[1, 1, 0], [1, 1, 1], [0, 1, 1]]))