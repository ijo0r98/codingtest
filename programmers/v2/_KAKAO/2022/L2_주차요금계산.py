# 2022 KAKAO BLIND RECRUITMENT > 주차 요금 계산

import collections, math

def solution(fees, records):
    answer = []
    car_time = collections.defaultdict(list)
    
    for record in records:
        info = record.split() # 시간, 차번호, 입출차
        car_time[info[1]].append(info[0])
    
    for key, itm in car_time.items():
        total_m = 0
        if len(itm) % 2 == 0:
            for i in range(0, len(itm), 2):
                h1, m1 = int(itm[i][:2]), int(itm[i][-2:])
                h2, m2 = int(itm[i+1][:2]), int(itm[i+1][-2:])
                if m2 > m1:
                    diff = m2-m1
                    diff += (h2-h1) * 60
                else:
                    diff = (60+m2)-m1
                    diff += (h2-1-h1) * 60
                total_m += diff
        else: 
            for i in range(0, len(itm)-1, 2):
                h1, m1 = int(itm[i][:2]), int(itm[i][-2:])
                h2, m2 = int(itm[i+1][:2]), int(itm[i+1][-2:])
                if m2 > m1:
                    diff = m2-m1
                    diff += (h2-h1) * 60
                else:
                    diff = (60+m2)-m1
                    diff += (h2-1-h1) * 60
                total_m += diff
                
            last_h, last_m = int(itm[-1][:2]), int(itm[-1][-2:])
            total_m = total_m + (59-last_m) + (23-last_h)*60
        
        # fees [기본시간, 기본요금, 단위시간, 단위요금]
        fee = fees[1]
        if total_m > fees[0]:
            fee += math.ceil((total_m-fees[0])/fees[2]) * fees[3]
        answer.append((key, fee))
        
    answer.sort(key=lambda x: x[0])
    
    return list(map(lambda x: x[1], answer))