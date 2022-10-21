
T = int(input())
a = []
b = []
count = 0
for i in range(T):
    word = input()
    n = word[0]
    w = ''.join(dict.fromkeys(word))#입력 순서 유지하고 중복글자 제거
    b.append(w) #중복 제거한 문자열을 b에저장
    #연속된 중복문자 제거한 후에 한 단어에 문자가 한개씩면 쓰인건지 확인
    for i in range(1, len(word)):
        if n[-1] == word[i]:
            continue
        else:
            n = n + word[i]
        #acabc 가 입력되면 acb로 n에 저장
    a.append(n)

for i in range(T):
    if a[i] == b[i]:
        count = count + 1

print(count)