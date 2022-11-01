import itertools
T = int(input())
for i in range(T):
    n = int(input())

    tri = []
    i = 1
    while True:
        if i*(i+1)//2 <= 1000:
            tri.append(i*(i+1)//2)
            i += 1
        else:
            break

    data = itertools.combinations_with_replacement(tri, 3)
    f = []

    for i in data:
        f.append(sum(i))

    if n in f:
        print("1")
    else:
        print("0")