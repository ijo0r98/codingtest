# 고득점 kit > hash > 베스트앨범(L3)

# * 장르별 2곡씩
# 1) 속한 노래가 많이 재생된 장르 먼저 수록
# 2) 장르 내에서 많이 재생된 노래 먼저 수록
# 3) 장르 내에서 재생 횟수가 같은 노래 중, 고유 번호가 낮은 노래 먼저 수록

# 1
from collections import defaultdict

def solution(genres, plays):
    answer = []
    
    # for g in genres_list:
    #     genres_dict[g] = 0
    genres_dict = defaultdict(int)
    plays_dict = defaultdict(list)
    
    for i, [g, p] in enumerate(zip(genres, plays)):
        genres_dict[g] += p
        plays_dict[g].append((i, plays[i])) # tuple
    
    genres_dict = sorted(genres_dict.items(), key=lambda item: item[1], reverse=True)

    # for value in plays_dict.values():
    #     value.sort(key=lambda x: x[1], reverse=True)

    for key, value in genres_dict:
        musics = sorted(plays_dict[key], key=lambda x: x[1], reverse=True)[:2]
        for _, i in musics:
            answer.append(_)
        
    return answer


#####
g = ["classic", "pop", "classic", "classic", "pop"]
p = [500, 600, 150, 800, 2500]
print(solution(g, p)) # [4, 1, 3, 0]

g2 = ["A", "A", "B", "A", "B", "B", "A", "A", "A", "A"]
p2 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1] 
print(solution(g2, p2)) # [0, 1, 2, 4]