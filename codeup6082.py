
nlist =[]
new_list = []


#입력한 숫자까지 리스트를 만들어서 nlist에 저장
n = int(input())
for i in range(1, n+1):
    nlist.append(i)
print(nlist)


#nlist 형을 숫자에서 문자열 리스트로 변환
nlist = str(nlist)
print("숫자 리스트를 문자열 리스트로 변횐:\n", nlist)


#nlist에서 문자'3'을 포함하는 문자열 출력
#여기서 오류가 난다!!! 내가 원하는 출력은 n이 13일 경우에 
#'3', '13'이 출력되어야 하는데, '3', '3'이 출력된다.
matching = [s for s in nlist if '3' in s]
print(matching)

# '3'을 포함하고 있는 문자열의 인덱스 값을 가져온다.
# 출력값이 2와 12가 나와야 하는데 7,41로 나온다.
find_number = '3'
numbers = [i for i in range(len(nlist)) if find_number in nlist[i]]
print(numbers)


#만약 3이 포함된 문자열이 nlist안에 있으면 해당 문자열을 new_list의 새로운 원소로 추가한다.
#기대하는 출력값은 위와 같이 3,13인다 3,3이 나온다.
for word in nlist:
    if '3' in word:
        new_list.append(word)
print(new_list)
#result = ' '.join(str(s) for s in nlist)
#print(result)

#str_list = ['There', 'is', 4, "items"]
#str_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
#result = ' '.join(str(s) for s in str_list)
#print(result)


#print(nlist[2])
def listToString(nlist):
    result = ""
    for s in nlist:
        result += s + ""
    return result.strip()

result = listToString(nlist)
print(result)

"""
n =int(input())
for i in range(1, n+1):
    if i%10 == 3: # 3, 13, 23, 33 ...
        print("X", end=' ')
    elif i%10 == 6:
        print("X", end=' ')
    elif i%10 == 9:
        print("X", end=' ')
    else:
        print(i, end=' ')
"""

"""
nlist = []
str_nlist = []
idx = []


#입력한 숫자까지 리스트를 만들어서 nlist에 저장
n = int(input())
for i in range(1, n+1):
    nlist.append(i)
print(nlist)


#nlist 형을 숫자에서 문자열 리스트로 변환
for n in nlist:
    str_nlist.append(str(n))
#nlist = str(nlist)
print("숫자 리스트를 문자열 리스트로 변횐:\n", str_nlist)

for s in range(len(str_nlist)):
    tmp = ''
    for i in range(len(str_nlist[s])):
        if str_nlist[s][i] == '3':
            tmp += 'X'
        else:
            tmp += str_nlist[s][i]
    str_nlist[s] = tmp
    print('잘 바뀜?', tmp)
print('잘 바뀜?', str_nlist)
"""