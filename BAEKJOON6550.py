
"""
while True:
    try:
        s, t = map(str, sys.stdin.readline().split())

        if s in t:
            print("Yes")
        else:
            sword = []
             tword = []
            for i in range(len(s)):
                for j in range(i, len(t)):
                    if s[i] == t[j]:
                        print(i)
                        print(j)
                        print(t[j])
                        if i <= j:
                            sword.append(s[i])
                            tword.append(t[j])
                            print("i의 값", i, "s[i]의 값", s[i])
                            print("j의 값", j, "t[j]의 값", t[j])
                            break
                        else:
                            break
            jsword = "".join(sword)
            jtword = "".join(tword)
            print("s의 값:", jsword)
            print("추출한 t의 값:",jtword)
            if jsword == s:
                print("Yes")
            else:
                print("No")
    except:
        break
"""
"""
s, t = map(str, sys.stdin.readline().split())

if s in t:
    print("Yes")
else:
    sword = []
    tword = []
    for i in range(len(s)):
        for j in range(i, len(t)):
            if s[i] == t[j]:
                print(i)
                print(j)
                print(t[j])
                sword.append(s[i])
                tword.append(t[j])
                print("i의 값", i, "s[i]의 값", s[i])
                print("j의 값", j, "t[j]의 값", t[j])
                break
    jsword = "".join(sword)
    jtword = "".join(tword)
    print("추출한 s의 값:", jsword)
    print("추출한 t의 값:",jtword)
    if jsword == s:
        print("Yes")
    else:
        print("No")
"""
"""
jlist = 0
ns = []

for i in range(len(s)):
    for j in range(jlist, len(t)):
        if s[i] == t[j]:
            ns.append(s[i])
            jlist = j
            break

if s in t:
    print("Yes")
elif ("".join(ns)) == s:
    print("Yes")
else:
    print("No")
"""
"""
while True:
    try:
        s, t = input().split()
        jindex = 0
        new_s = []

        for i in range(len(s)):
            for j in range(jindex+1, len(t)):
                if s[i] == t[0]:
                    new_s.append(s[i])
                    break
                elif s[i] == t[j]:
                    new_s.append(s[i])
                    jindex = j
                    break
        if s in t:
            print("Yes")
        elif ("".join(new_s)) == s:
            print("Yes")
        else:
            print("No")
    except EOFError:
        break
"""
"""
s, t = input().split()
jindex = 0
new_s = []

for i in range(len(s)):
    for j in range(jindex+1, len(t)):
        if s[i] == t[0]:
            new_s.append(s[i])
            print(i, s[i], j, t[j])
            break
        elif s[i] == t[j]:
            new_s.append(s[i])
            jindex = j
            print(i, s[i], j, t[j])
            break

if s in t:
    print("Yes")
elif ("".join(new_s)) == s:
    print("Yes")
else:
    print("No")
"""
"""
s, t = input().split()
index = 0
new_s = []

for i in range(len(s)):
    for j in range(index, len(t)):
        if  s[i] == t[j]:
            print("s[{}]: {}, t[{}]: {}".format(i, s[i], j, t[j],))
            new_s.append(s[i])
            print("new_s:{}".format(new_s))
            index = j + 1
            print("index:{}, j:{}".format(index, j))
            print(s[i])
            break
print("s와 동일한 마지막 t의 인덱스:", j)
print("입력한 s의 길이:", len(s))
print("마지막 t의 인덱스에서 입력한 s의 길이를 빼면 부분 문자열인 경우 중복이 시작되는 t의 인덱스:", j -len(s)+1)
print(t[j-len(s)+1:j+1])
print(new_s)
print("".join(new_s))

if ("".join(new_s) == (t[j-len(s)+1:j+1])):
    print("YES")
else:
    print("NO")
"""


while True:
    try:
        s, t = input().split()
        index = 0
        new_s = []

        for i in range(len(s)):
            for j in range(index, len(t)):
                if  s[i] == t[j]:
                    new_s.append(s[i])
                    index = j + 1
                    break

        if ("".join(new_s)) == s:
            print("Yes")
        else:
            print("No")
    except:
        break

"""
while True:
    try:
        s, t = input().split()
        value = 0
        flag = 0
        for i in range(len(t)):
            if t[i] == s[value]:
                value = value + 1
                if value == len(s):
                    flag = 1
                    break
        if flag == 1:
            print("Yes")
        else:
            print("No")
    except:
        break
"""