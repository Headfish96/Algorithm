S = input()
K = input()

new_S = ''.join(i for i in S if not i.isdigit())

if K in new_S:
    print("1")
else:
    print("0")

"""
for i in my_string:
    if no x.isdigit():
        x

keyword = []
for i in range(len(K)):
    for j in range(len(S)):
        if K[i] == S[j]:
            keyword.append(S[j])

if len(keyword) == len(K):
    if K in S:
        print("1")
    else:
        print("0")
else:
    print("0")
"""