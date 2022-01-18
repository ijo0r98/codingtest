# 0117

# 1 -> 55% 가장 작은 양의 정수를 출력해야 함(빼열에 속한 수보다 작은 수도 가능)
def solution(A):
    A = sorted(A)
    if A[-1] < 0 : # 배열이 모두 음수로 이뤄져있을 때
        return 1
    for i in range(len(A)-1):
        if (A[i] > 0) and ((A[i+1] - A[i]) > 1):
            return A[i]+1
    
    return A[-1]+1

# 2 -> 88% 양수 & 음수 섞인 경우 생각 x
def solution(A):
    A = sorted(A)
    if (A[-1] < 0) or (A[0] > 1):
        # 배열이 모두 음수로 이뤄져있을 때 & 1로 시작하지 않을 때 1이 가장 작은 양의 정수
        return 1
    for i in range(len(A)-1):
        if (A[i] > 0) and ((A[i+1] - A[i]) > 1):
            return A[i]+1
    
    return A[-1]+1

# 3 -> 100%, O(N) or O(N * log(N))
def solution(A):
    new_A = []
    
    for a in A:
        if a > 0:
            new_A.append(a)
    new_A = sorted(new_A)        
            
    if (len(new_A) == 0) or (new_A[0] > 1):
        return 1
    
    for i in range(len(new_A)-1):
        if (new_A[i+1] - new_A[i]) > 1:
            return new_A[i]+1
    
    return new_A[-1]+1


# 다른 사람 풀이 1 (https://sooho-kim.tistory.com/33, O(N) or O(N * log(N)))
def solution(N, A):
    A.sort()
    A = list(set(A))
    missingdata = 1
    for i in A:
        if i == missingdata :
            missingdata +=1
    return missingdata

# 다른 사람 풀이 2 (https://this-programmer.tistory.com/342)
def solution(A):
    temp_list = {*list(range(1, max(A) + 2))}
    for i in A:
        if i in temp_list:
            temp_list.remove(i)
    return min(temp_list) if temp_list and min(temp_list) > 0 else 1

print(solution([1, 3, 6, 4, 1, 2])) # 5
print(solution([-4, -3, -2, -1])) # 1
print(solution([-4, -3, -2, 1])) # 2
print(solution([2])) # 1
print(solution([-1000, 1000])) # 1