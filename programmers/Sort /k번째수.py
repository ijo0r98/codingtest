# 고득점 kit > 정렬 > k번째수(L1)

# 1
def solution(array, commands):
    answer = []
    
    for start, end, idx in commands:
        answer.append(array[start - 1])
        new_array = array[start - 1 : end]
        answer.append(sorted(new_array)[idx - 1])
        
    return answer


# 2
def solution(array, commands):
    return list(map(lambda x:sorted(array[x[0]-1:x[1]])[x[2]-1], commands))

#####
array, commands = [1, 5, 2, 6, 3, 7, 4], [[2, 5, 3], [4, 4, 1], [1, 7, 3]]
print(solution(array, commands)) # [5, 6, 3]