n = int(input(), 16)

for i in range(1, 16):
    sixteen = n*i
    print('%X'%n, '*', '%X'%i, '=', '%X'%sixteen, sep = '')
