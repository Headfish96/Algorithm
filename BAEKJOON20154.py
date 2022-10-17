alphabet = dict()
alphabet = { 'A':3, 'B':2, 'C':1, 'D':2, 'E':3, 'F':3, 'G':3, 'H':3, 'I':1,
'J':1, 'K':3, 'L':1, 'M':3, 'N':3, 'O':1, 'P':2, 'Q':2, 'R':2, 'S':1, 'T':2, 'U':1,
'V':1, 'W':2, 'X':2, 'Y':2, 'Z':1 } 

S = input()
S = list(S)

v_list = []
for i in S:
    if i in alphabet:
        value = alphabet[i]
        v_list.append(value)

if (sum(v_list)%10)%2 == 1:
    print("I'm a winner!")
else:
    print("You're the winner?")
"""
while len(v_list) >= 1:
    if len(v_list)%2 == 1:
        for i in range((len(v_list)//2) -1):
            v_list[len(v_list)//2] = v_list[-1]
            v_list[i] = sum(v_list[i*2: 1*2+2])
            #del v_list[(len(v_list)//2+1):]
    else:
        for i in range(len(v_list)//2):
            v_list[len(v_list)//2] = v_list[-1]
            v_list[i] = sum(v_list[i*2: 1*2+2])
            #del v_list[(len(v_list)//2):]
    print(v_list)    

           
            del v_list[]
v_list[0] = sum(v_list[0:2])
v_list[1] = sum(v_list[2:4])
v_list[2] = sum(v_list[4:6])
v_list[3] = v_list[-1]
del v_list[4]
del v_list[5]

print(v_list)

sum = 0
sumlist = []
if K%2 == 1:
    for i in range(K//2):
        sum = (alphabet[S[i*2]] + alphabet[S[i*2+1]])%10
        sumlist.append(sum)
    sum = alphabet[S[-1]]
    sumlist.append(sum)
    print(sumlist)

    for i in range(len(sumlist)//2):
        sum = (sumlist[i*2] + sumlist[i*2+1])%10
        sumlist[i] = sum
    sum = sumlist[-1]
    sumlist.append(sum)
    print(sumlist)
"""

