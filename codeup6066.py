"""
a, b, c = input().split()
a = int(a)
b = int(b)
c = int(c)

if a%2 == 0:
    print("even")
else:
    print("odd")
"""
number = list(map(int, input().split()))

for i in range(len(number)):
    if number[i]%2 == 0:
        print("even")
    else:
        print("odd")
