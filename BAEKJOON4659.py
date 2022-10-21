from unittest import result


pw = []
while True:
    a = input()
    pw.append(a)
    if pw[-1] == 'end':
        break
    else:
        continue

w = []
a = []
for i in range(len(pw)-1): #연속한 중복 문자 제거
    n = pw[i][0]
    for j in range(1, len(pw[i])):
        if n[-1] == pw[i][j]:
            continue
        else:
            n = n + pw[i][j]
    w.append(n)

m = []
vowels = 'aeiou'
z = []
for i in range(len(pw)-1): #단어에서 모음을 제거
    n = []
    x = []
    #n = pw[i][0] #n은 pw의 첫번째 단어의 첫 글자
    for j in range(0, len(pw[i])):
        if pw[i][j] not in vowels:
            #n = n + pw[i][j]
            n.append(pw[i][j])
        elif pw[i][j] in vowels:
            x.append(j) #한 단어의 모음이 들어간 위치의 인덱스
    
    m.append(''.join(n))
    z.append(x)

print(pw)
print(w)
print(m)
print(z)
print(x)
print(z[-1])
for i in range(len(z)):
    print(int(z[i][-1]) - int(z[i][0]))

for i in range(len(pw)-1): #단어에서 중복을 제오한 것들 중 모음을 반드시 1개 이상 포함하는지 확인
    if pw[i] != w[i]:
        if ('ee' in pw[i] ) or ('oo' in pw[i]):
            print(True, pw[i])
        else:
            print(False, pw[i])
    elif pw[i] == w[i]:
        if ('a' in pw[i]) or ('e' in pw[i]) or ('i' in pw[i]) or ('o' in pw[i]) or ('u'in pw[i]):
            print(True, pw[i])
        else:
            print(False, pw[i])
