import sys

x,y,p1,p2 = map(int, sys.stdin.readline().split())
print(x,y,p1,p2)

s = []
for i in range(100):
    a = x*i + p1
    for j in range(100):
        b = y*j + p2
        if a == b:
            s.append(a)


if len(s) == 0:
    print('-1')
else:
    print(min(s))