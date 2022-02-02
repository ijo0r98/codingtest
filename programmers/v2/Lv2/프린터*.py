# 스택/큐 > 프린터

# 1
def solution(priorities, location):
    waits = []
    for idx, p in enumerate(priorities):
        waits.append((idx, p))
        if idx == location:
            find = waits[-1]

    waits.sort(key=lambda x: x[1], reverse=True)
    
    return waits.index(find) + 1
        

# 2
def solution(priorities, location):
    max_p = max(priorities)
    docs = []
    waits = []
    
    for idx, p in enumerate(priorities):
        docs.append((idx, p))
        if idx == location:
            find = (idx, p)
            
    while docs:
        doc = docs.pop(0)
        if doc[1] < max_p:
            docs.append(doc)
        else: 
            waits.append(doc)
        
    return waits.index(find) + 1
        

# 3 기존 코드 참고해서 품 ㅠ
def solution(priorities, location):
    waits = []
    docs = []

    for idx, p in enumerate(priorities):
        docs.append((idx, p)) 
        if idx == location: 
            find = (idx, p)

    while docs:
        max_p = max(p for _, p in docs)
        doc  = docs.pop(0)
        if doc[1] < max_p: 
            docs.append(doc)
        else: 
            waits.append(doc)

    return waits.index(find) + 1 