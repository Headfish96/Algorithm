a = int(input())
sumN = 0
for i in range(1, a):
    sumN = sumN + i
    if sumN >= a:
        break
print(i)
