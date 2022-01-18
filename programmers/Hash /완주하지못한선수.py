# 고득점 kit > hash > 완주하지 못한 선수(L1)

# 1
def solution(participant, completion):
    answer = ''
    
    for p in participant:
        if p in completion:
            completion.remove(p)
        else:
            answer = p
            
    return answer


# 2
def solution(participant, completion):
    answer = ''
    dict = {}
    temp = 0
    
    for p in participant:
        dict[hash(p)] = p
        temp += int(hash(p))

    for c in completion:
        temp -= int(hash(c))
    
    answer = dict[temp]

    return answer


# 3
import collections

def solution(participant, completion):
    answer = collections.Counter(participant) - collections.Counter(completion)
    return list(answer.keys())[0]


# 4
def solution(participant, completion):
    participant.sort()
    completion.sort()

    for i in range(len(completion)):
        if participant[i] != completion[i]:
            return participant[i]

    return participant[len(participant)-1]


# 5
def solution(participant, completion):
    participant.sort()
    completion.sort()

    for p, c in zip(participant, completion):
        if p != c:
            return p
    return participant[-1]



#####
p = ['marina', "josipa", "nikola", "vinko", "filipa"]
c = ["josipa", "filipa", "marina", "nikola"]
print(solution(p, c))
