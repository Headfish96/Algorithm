
"""
n = int(sys.stdin.readline())
data = [sys.stdin.readline().strip() for i in range(n)]
print(data)
"""
"""
def secret():
    data = []
    while True:
        i = 0
        i = i + 1
        data = sys.stdin.readline().strip()
        if data[-1] == 'END':
            break
    return data

print(secret())
"""
"""
i = 0
list = []
list.append(0)
while True:
    i = i + 1
    list.append(i)
    end = input()
    if end == 'END':
        break
    print(list)
"""
import sys

i = 0
data = []
while True:
    i = i + 1
    data.append(sys.stdin.readline().strip())
    if data[-1] == 'END':
        break
#입력된 data 전부 출력
#enumeratate 사용법 익히기 
for i in range(len(data) - 1):
    data[i] = data[i][::-1]

for i in range(len(data) - 1):
    print(data[i])
"""
#입력된 data중에 0번째 원소만 리스트로 data_list1로 저장
data_list1 = list(data[0])
print(data_list1)

#data_list1을 뒤집음
data_list1.reverse()
print(data_list1)

#뒤집은 data_list1을 다시 합친다
data_list1 = ''.join(data_list1)
print(data_list1)

print(len(data))
data_list = []
#data_list = list(data[i])
for i in range(len(data) - 1):
    data_list.append(list(data[i]))
 
data_list[0].reverse()
print(data_list[0])

data_list[0] = ''.join(data_list[0])
print(data_list[0])

for i in range(len(data) - 1):
    data_list[i].reverse()
    data_list[i] = ''.join(data_list[i])
    print(data_list[i])
"""