"""
#오답 1. 시간초과
import sys

N, M = map(int, sys.stdin.readline().split())
never = []
for i in range(N+M):
    never.append(sys.stdin.readline().rstrip())

print(len(sorted(set(never[:N]) & set(never[N:]))))
for i in range(len(sorted(set(never[:N]) & set(never[N:])))):
    print(sorted(set(never[:N]) & set(never[N:]))[i])
"""

"""
#정답
import sys
N, M = map(int, sys.stdin.readline().split())
neverheard = []
neverseen = []
neverheardandseen = []

for i in range(N):
    neverheard.append(input())
for i in range(M):
    neverseen.append(input())

neverheardandseen = set(neverheard) & set(neverseen)

print(len(neverheardandseen))
for x in sorted(neverheardandseen):
    print(x)
"""



#오답 2
import sys
N, M = map(int, sys.stdin.readline().split())

nheard = []
nseen = []
nheardnseen = []

for i in range(N):
    nheard.append(input())
for i in range(M):
    nseen.append(input())

for i in range(N):
    for j in range(M):
        if nheard[i] == nseen[j]:
            nheardnseen.append(nheard[i])

print(len(sorted(nheardnseen)))
for x in sorted(nheardnseen):
    print(x)
