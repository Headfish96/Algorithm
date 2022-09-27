#1초동안 마이크로 소리 강약을 체크하는 횟수를 h
#한번 체크한 값을 저장할 때 사용하는 비트수를 b

h, b, c, s = input().split()
h = int(h)
b = int(b)
c = int(c)
s = int(s)
#print('%.2f' %t)

#print("Hz:", h, "Bit:", b, "Channel:", c, "Second:", s)

total = (h*b*c*s)/8
print(total)

kb = total/1024
#print("킬로바이트: ", kb)

mb = kb/1024
print('%.1f' %mb, "MB")