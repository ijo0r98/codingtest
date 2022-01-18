# 1175. 단어 공부

from collections import defaultdict

string = input().lower()
cnt_dict = defaultdict(int)
max_cnt = 0
for s in string:
    cnt_dict[s] += 1
    max_cnt = max(max_cnt, cnt_dict[s])
   
max_array = []
for item in cnt_dict.items():
    if max_cnt == item[1]:
        max_array.append(item[0])
        
if len(max_array) > 1:
    print('?')
else:
    print(max_array[0].upper())