N = int(input())
word = []

for i in range(N):
    a = input()
    if a not in word:
        word.append(a)


word.sort()
word.sort(key=len)

for i in range(len(word)):
    print(word[i])
"""
for i in range(len(word)):
    for j in range(len(word) - i):
        if word[i] == word[j]:
"""

"""
T = int(input())
a = []
b = []
count = 0
for i in range(T):
    word = input()
    n = word[0]
    w = ''.join(dict.fromkeys(word))
    b.append(w)
    for i in range(1, len(word)):
        if n[-1] == word[i]:
            continue
        else:
            n = n + word[i]
    a.append(n)

for i in range(T):
    if a[i] == b[i]:
        count = count + 1
        
print(count)
"""