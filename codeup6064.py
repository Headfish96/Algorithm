a, b, c = input().split()
a = int(a)
b = int(b)
c = int(c)
print((a if (a<=b) else b) if ((a if (a<=b) else b) <= c) else c)
"""
print("a =", a, "b =", b, "c =", c)
x = a if (a < b) else b
print("x =", x)
y = x if (x < c) else c
print("y =", y)

if (a<b):
    print("a보다 b가 큼")
else:
    print("a가 b보다 크거나 같음")
"""

