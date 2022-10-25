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
T = int(input()) #테스트케이스의 수 입력받음

datas = [] #빈 리스트 선언

for i in range(T): #테스트 케이스의 수 만큼 반복

    #한줄씩 입력 받아서 datas에 넣어주는데, 공백은 없애고 넣는다.
    #asvdge ef ofmdofn 입력하면 공백을 빼고 asvdgeefofmdofn 이 datas에 저장된다.
    datas.append(sys.stdin.readline().strip().replace(" ",""))

    counts = dict() #counts라는 빈 딕셔너리를 선언해둔다.

    # data가 datas[i]에 있으면 아래 문장을 실행한다.
    # 예를 들어 T에 1이 들어오고 datas[0]에 asvdgeefofmdofn 가 저장되었으면
    for data in datas[i] :
        # a가 datas[0]에, 즉, asvdgeefofmdofn에 없음, counts[a] = 1
        # s
        # v
        # d
        # g
        # e가 datas[0]에, 즉 asvdgeefofmdofn에 없었음, 최초 등장임. counts[e] = 1
        if data not in counts: 
            counts[data] = 1
        else :
        # e가 datas[0]에, 즉 즉 asvdgeefofmdofn에 한번 있었음. 그래서 counts[e]에 +1
            counts[data] = counts[data] + 1
    
    #counts라는 딕셔너리의 '값', 즉 values만 all_values라는 리스트에 넣어준다.        
    all_values = counts.values()
    
    #list 선언을 통해 리스트 내의 값들 하나하나을 원소로 만들어준다.
    all_values = list(all_values)
    
    
    max_value = max(all_values) # 값들 중에서 최댓값을 찾는다

    #최댓값을 갖는 키를 찾는다.
    #get 함수를 이용하는 것에 주의!
    max_key = max(counts, key = counts.get)

    #만약 쵀댓값이 한개 이상이라면 ?를 출력
    if all_values.count(max_value) > 1:
        print("?")
    #최댓값이 한개라면 그 키를 출력
    else:
        print(max_key)
    
    