# 0117

def solution(X, A):
    # X가 강의길이일 때  1~5 모든 숫자가 나타났을 때 강을 건널 수 있음
    # each element of array A is an integer within the range [1..X].
    
    nums = set()
    for i in range(len(A)):
        nums.add(A[i])
        if len(nums) == X:
            break
        
    if (i == len(A)-1) and (len(nums) != X):
        i = -1
        
    return i
    
    
    
print(solution(5, [1, 3, 1, 4, 2, 3, 5, 4])) # 6
print(solution(5, [1, 3, 1, 4, 2, 3, 4])) # -1
print(solution(1, [1])) # 1
print(solution(2, [1])) # -1
