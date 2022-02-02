# 2021 카카오 채용연계형 인턴십 > 거리두기 확인하기

def solution(places):
    answer = []
    
    for k in range(5):
        candidates = []
        place = places[k]
        for i in range(5):
            for j in range(5):
                if place[i][j] == 'P':
                    candidates.append((i, j))
        
        ck = True
        for i in range(len(candidates)-1):
            for j in range(i+1, len(candidates)):
                x1, y1 = candidates[i][0], candidates[i][1]
                x2, y2 = candidates[j][0], candidates[j][1]
                dist = abs(x1-x2) + abs(y1-y2)
                if dist <= 2:
                    if (x1 != x2) and (y1 != y2):
                        if (place[x1][y2] != 'X') or (place[x2][y1] != 'X'):
                            ck = False
                            break
                    elif (x1==x2):
                        if place[x1][min(y1, y2)+1] != 'X':
                            ck = False
                            break
                    elif (y1==y2):
                        if place[min(x1, x2)+1][y1] != 'X':
                            ck = False
                            break
                        
        if ck:
            answer.append(1)
        else:
            answer.append(0)
            
    return answer