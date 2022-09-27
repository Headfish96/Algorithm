import math

#빨강, 파랑, 초록의 색은 3가지
#그리고 각 색의 가짓수를 지정할 수 있음
#지정된 가짓수에 따라 3개를 조합할 수 있는 수가 달라짐
#조합 가능한 수는 가짓수의 3승
#색의 가짓수가 2이면 2의 3승 8가지
#색의 가짓수가 3이면 3의 3승 27가지
"""
0 0 0
0 0 1
0 0 2
0 1 0
0 1 1
0 1 2
0 2 0
0 2 1
0 2 2

1 0 0
1 0 1
1 0 2
1 1 0
1 1 1
1 1 2
1 2 0
1 2 1
1 2 2

2 0 0
2 0 1
2 0 2
2 1 0
2 1 1
2 1 2
2 2 0
2 2 1
2 2 2
"""
"""
n = int(input())
m = int(math.pow(n, 3))
print(m)
"""
#세가지 색의 가짓수를 모두 다르게 입력할 경우
#xyz라고 하면 x*y*z 개가 된디ㅏ.

red, green, blue = input().split()
red = int(red)
green = int(green)
blue = int(blue)
total = red * green * blue

tlist = []
for i in range(red):
    for j in range(green):
        for k in range(blue): 
            print(i, j, k)
print(total)