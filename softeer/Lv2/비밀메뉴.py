import sys

m, n, k = map(int, input().split())
m_list = list(map(int, input().split())) # 비밀 메뉴 조작법
m_len = len(m_list)
n_list = list(map(int, input().split())) # 사용자 버튼 조작

index = [i for i in range(len(n_list)) if m_list[0] == n_list[i]]

def funtion1(m_list, n_list) :
    if len(n_list) < len(m_list) : return 'normal'
    if len(index) == 0: return 'normal'
    
    res = "secret"
    for i in range(len(index)): # 처음 시작 인덱스
        idx = index[i]
        for j in range(m_len): # 전체 같은지 비교
            res="secret"
            # print(i, j, idx, m_list[j], n_list[j+idx])
            if m_list[j] != n_list[j+idx] :
                res = "normal"
                break
            
        if (j==m_len-1) : return res
            
    return res
    
print(funtion1(m_list, n_list))