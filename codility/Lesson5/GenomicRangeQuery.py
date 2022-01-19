# 0118

# 1 시간복잡도 O(N*M)
def solution(S, P, Q):
    answer = []
    letters = {'A': 1, 'C': 2, 'G': 3, 'T': 4} 
 
    m = len(Q)
    for i in range(m):
        p, q = P[i], Q[i]
        tmp_s = S[p:(q+1)]
        tmp = 100
        for j in tmp_s:
            tmp = min(tmp, letters[j])
        answer.append(tmp)

    return answer

## 목표 시간복잡도 O(N+M)

# 2
def solution(S, P, Q):
    answer = []

    m = len(P)
    for i in range(m):
        p, q = P[i], Q[i]
        tmp_s = S[p:(q+1)]
        if 'A' in tmp_s:
            answer.append(1)
        elif 'C' in tmp_s:
            answer.append(2)           
        elif 'G' in tmp_s:
            answer.append(3)
        else:
            answer.append(4)
        
    return answer


# 다른 사람 풀이 1
def solution(S, P, Q):
    A, C, G, T = 0, 0, 0, 0

    cummulated = [[0, 0, 0, 0]]
    for char in S:
        if char == "A":
            A += 1
        elif char == "C":
            C += 1
        elif char == "G":
            G += 1
        elif char == "T":
            T += 1
        cummulated.append([A, C, G, T])

    i_f_table = {"A": 1, "C": 2, "G": 3, "T": 4}
    answer = []
    for p, q in zip(P, Q):
        left, right = cummulated[p], cummulated[q + 1]
        if left[0] != right[0]:
            answer.append(1)
        elif left[1] != right[1]:
            answer.append(2)
        elif left[2] != right[2]:
            answer.append(3)
        elif left[3] != right[3]:
            answer.append(4)
        else:
            answer.append(i_f_table[S[p]])
    return answer

# 다른 사람 풀이 2
def solution(S, P, Q):
    M = len(P)
    N = len(S)
    A = [[0, 0, 0, 0]]
    counter = [0] * 4
    result = []
    for i in S:
        if i == "A":
            counter[0] += 1
            A.append(counter[:])
        elif i == "C":
            counter[1] += 1
            A.append(counter[:])
        elif i == "G":
            counter[2] += 1
            A.append(counter[:])
        elif i == "T":
            counter[3] += 1
            A.append(counter[:])
    
    for i in range(M):
        for j in range(4):
            val = A[Q[i]+1][j] - A[P[i]][j]
            if val != 0:
                result.append(j + 1)
                break
    
    return result


print(solution('CAGCCTA', [2, 5, 0], [4, 5, 6]))