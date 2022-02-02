# 2019 KAKAO BLIND RECRUITMENT > 오픈채팅방

def solution(records):
    user = {}
    answer = []
    
    for record in records:
        record = record.split()
        if (record[0] == 'Enter') or (record[0] == 'Change'):
            user[record[1]] = record[2]
        
    for record in records:
        record = record.split()
        if record[0] == 'Enter':
            answer.append(user[record[1]] + "님이 들어왔습니다.")
        elif record[0] == 'Leave':
            answer.append(user[record[1]] + "님이 나갔습니다.")
    
    return answer
            