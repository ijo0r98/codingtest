# 고득점 kit > 정렬 > H-Index(L2)

# 어떤 과학자가 발표한 논문 n편 중, h번 이상 인용된 논문이 h편 이상이고 나머지 논문이 h번 이하 인용되었다면 h의 최댓값이 이 과학자의 H-Index입니다.

# 1
def solution(citations):
    answer = 0

    for h in range(max(citations), -1, -1):
        cited_more = list(c for c in citations if c >= h) # h번 이상 인용된 논문 수
        if len(cited_more) >= h: # h편 이상일때
            return h


# 2
def solution(citations):
    citations.sort(reverse=True)
    answer = max(map(min, enumerate(citations, start=1)))
    return answer



#####
print('answer: ', solution([3, 0, 6, 1, 5])) # 3
print('answer: ', solution([5, 5, 5, 5])) # 4
print('answer: ', solution([5, 5, 5, 5, 5])) # 5
print('answer: ', solution([0, 0, 0])) # 0
print('answer: ', solution([0, 1, 2])) # 1
