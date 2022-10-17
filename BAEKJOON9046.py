"""
from itertools import count
import sys
T = int(input())
#print(T, "줄 입력")

datas = []
for i in range(T):
    datas.append(sys.stdin.readline().strip().replace(" ",""))
#print("datas 리스트 출력:", datas)

data_list = []
for i in range(T):
    data_list.append(list(datas[i]))
#print("data_list 리스트 출력", data_list)

counts = dict()
for i in range(T):
    for data in data_list[i] :
        if data not in counts: 
            counts[data] = 1
        else :
            counts[data] = counts[data] + 1
            
    all_values = counts.values() #counts의 값들 전체, 즉, data에 들어간 문자들의 빈도수 전체
    all_values = list(all_values)
    #print(all_values)
    #for p in enumerate(all_values):
        #print(p)
    max_value = max(all_values) #가장 높은 빈도수, 값을 가진 것을 찾음
    max_key = max(counts, key = counts.get) #가장 높은 빈도수를 가지는 key값 찾음
    if all_values.count(max_value) > 1:
        print("?")
    else:
        print(max_key) #가장 높은 빈도수를 가지는 key값 출력
    
    from itertools import count
"""

import sys
T = int(input())

datas = []
"""
for i in range(T):
    datas.append(sys.stdin.readline().strip().replace(" ",""))
"""
for i in range(T):
    datas.append(sys.stdin.readline().strip().replace(" ",""))
    counts = dict() #초기화 문제 이해가 안간다.
    for data in datas[i] :
        if data not in counts: 
            counts[data] = 1
        else :
            counts[data] = counts[data] + 1
            
    all_values = counts.values()
    all_values = list(all_values)

    max_value = max(all_values)
    max_key = max(counts, key = counts.get)
    if all_values.count(max_value) > 1:
        print("?")
    else:
        print(max_key)
    
    