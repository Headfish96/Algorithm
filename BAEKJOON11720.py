"""
N = int(input())
number = input()
number_list = list(map(int, number))
sum = 0
for i in range(N):
    sum = sum + number_list[i]

print(sum)
"""
#map은 리스트의 요소를 지정된 함수로 처리해주는 함수이다.
N = int(input())
number = input()
#number_list = list(map(int, number))
sum = 0
for i in range(N):
    sum = sum + int(number[i])

print(sum)