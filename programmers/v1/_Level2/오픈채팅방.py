# 코딩테스트 연습 > 2019 KAKAO BLIND RECRUITMENT > 오픈채팅방

# def solution(records):
    
#     answer = [] 
#     change_names = {}
#     records.reverse()
#     records = [record.split() for record in records]

#     for i in range(len(records)):
#         record = records[i]
#         act = record[0]
#         id = record[1]

#         if act == 'Change':
#             if id in change_names.keys():
#                 continue
#             else:
#                 change_names[id] = record[2]
#         elif act == 'Enter': # 퇴장시에는 이름이 주어지지 않음
#             if id not in change_names:
#                 change_names[id] = record[2]
#             records[i][2] = record[2] if id not in change_names.keys() else change_names[id]
    
#     for record in records[::-1]:
#         if record[0] == 'Change':
#             continue
#         elif record[0] == 'Enter':
#             answer.append(record[2] + '님이 들어왔습니다.')
#         elif record[0] == 'Leave':
#             answer.append(change_names[record[1]] + '님이 나갔습니다.')

#     return answer


def solution(records):
    
    answer = [] 
    change_names = {}
    records = [record.split() for record in records]

    # 첫번째 for문에서 굳이 이름을 바꾸지 않고 아이디&이름 정보만 저장
    for record in records:
        if record[0] == 'Change':
            change_names[record[1]] = record[2] # change 이름 변경
        elif record[0] == 'Enter': # 퇴장시에는 이름이 주어지지 않음
            change_names[record[1]] = record[2]
    
    for record in records:
        if record[0] == 'Change':
            continue
        elif record[0] == 'Enter':
            answer.append(change_names[record[1]] + '님이 들어왔습니다.')
        elif record[0] == 'Leave':
            answer.append(change_names[record[1]] + '님이 나갔습니다.')

    return answer


print(solution(["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]))
# ["Prodo님이 들어왔습니다.", "Ryan님이 들어왔습니다.", "Prodo님이 나갔습니다.", "Prodo님이 들어왔습니다."]