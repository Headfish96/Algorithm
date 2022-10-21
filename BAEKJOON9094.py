"""
문제
두 정수 n과 m이 주어졌을 때,
0 < a < b < n인 정수 쌍 (a, b) 중에서 (a2+b2+m)/(ab)가 정수인 쌍의 개수를 구하는
프로그램을 작성하시오.

입력
첫째 줄에 테스트 케이스의 개수 T가 주어진다.
각 테스트 케이스는 한 줄로 이루어져 있으며, n과 m이 주어진다. 두 수는 0보다 크고, 100보다 작거나 같다.

출력
각 테스트 케이스마다 문제의 조건을 만족하는 (a, b)쌍의 개수를 출력한다.

예제 입력 1
3
10 1
20 3
30 4
예제 출력 1
2
4
5
"""
from itertools import combinations
#테스트 케이스의 수 입력받음
T = int(input())
N = []
n = []
for i in range(T):
    n, m = input().split()
    m = int(m)
    N.append((n,m))

brr = []
for i in range(T):
    arr = [] 
    for j in range(1, int(N[i][0])):
        arr.append(j)    # append로 요소 추가
    brr.append(arr)

crr = []
for i in range(len(brr)):
    crr.append(list(combinations(brr[i], 2)))

drr = []
for i in range(len(crr)):
    count = 0
    for j in range(0, len(crr[i])):
        a = int(crr[i][j][0])
        b = int(crr[i][j][1])
        c = (a*a + b*b + m)%(a*b)
        
        if c == 0:
            print(a,b)
            count = count + 1
    drr.append(count)

for i in range(len(drr)):
    print(drr[i])
