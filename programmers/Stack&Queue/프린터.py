# 고득점 kit > stack&queue > 프린터(L2)

# 1
def solution(priorities, location):
    answer = []

    docs = []
    find = ()

    for i, p in enumerate(priorities):
        docs.append((i, p)) # tuple(문서 인덱스, 우선순위)
        if i == location:
            find = (i, p)

    while len(docs) != 0:
        max_priority = max(p for _, p in docs)
        doc  = docs.pop(0)
        
        if doc[1] < max_priority: 
            docs.append(doc)
        else:
            answer.append(doc)

    return answer.index(find) + 1


# 2
def solution(priorities, location):
    queue =  [(i,p) for i,p in enumerate(priorities)]
    answer = 0

    while True:
        cur = queue.pop(0)
        if any(cur[1] < q[1] for q in queue):
            queue.append(cur)
        else:
            answer += 1
            if cur[0] == location:
                return answer


# 3
def solution(p, l):
    ans = 0
    m = max(p)
    while True:
        v = p.pop(0)
        if m == v:
            ans += 1
            if l == 0:
                break
            else:
                l -= 1
            m = max(p)
        else:
            p.append(v)
            if l == 0:
                l = len(p)-1
            else:
                l -= 1
    return ans



#####
p1, l1 = [2, 1, 3, 2], 2
print(solution(p1, l1))# 1

p2, l2 = [1, 1, 9, 1, 1, 1], 0
print(solution(p2, l2))# 5