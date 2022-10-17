"""
currnettime = input()
currnethour = int(currnettime[0:2])
currnetmin = int(currnettime[3:5])
currnetsec = int(currnettime[6:8])

Jtime = input()
Jhour = int(Jtime[0:2])
Jmin = int(Jtime[3:5])
Jsec = int(Jtime[6:8])

waithour = Jhour - currnethour
waitmin = Jmin - currnetmin
waitsec = Jsec - currnetsec

if (waithour >= 0) & (waitmin >= 0) & (waitsec < 0):
    waitmin = waitmin - 1
    waitsec = waitsec + 60
elif (waithour >= 0) & (waitmin < 0) & (waitsec < 0):
    waithour = waithour - 1
    waitmin = waitmin + 60 - 1
    waitsec = waitsec + 60
elif (waithour >= 0) & (waitmin < 0) & (waitsec >= 0):
    waithour = waithour - 1
    waitmin = waitmin + 60
elif (waithour < 0) & (waitmin >= 0) & (waitsec >= 0):
    waithour = waithour + 24
elif (waithour < 0) & (waitmin >= 0) & (waitsec < 0):
    waithour = waithour + 24
    waitmin = waitmin - 1
    waitsec = waitsec + 60
elif (waithour < 0) & (waitmin < 0) & (waitsec < 0):
    waithour = waithour + 24 - 1
    waitmin = waitmin + 60 - 1
    waitsec = waitsec + 60
    #예를 들어 03:15:20 - 20:18:35 = 6:57:45:
elif (waithour < 0) & (waitmin < 0) & (waitsec >= 0):
    waithour = waithour + 24 - 1
    waitmin = waitmin + 60
else:
  pass

waithour = '%02d' %waithour
waitmin = '%02d' %waitmin
waitsec = '%02d' %waitsec

resttime = waithour + ':' + waitmin + ':' + waitsec
print(resttime)
"""

def totalsec():
    time = input().split(':')
    time_hh = int(time[0])
    time_mm = int(time[1])
    time_ss = int(time[2])
    time_totalsec = (time_hh * 3600) + (time_mm * 60) + time_ss
    return time_totalsec

def resttime():
    ntime = totalsec()
    jtime = totalsec()
    rtime = jtime - ntime
    if rtime < 0:
        rtime = rtime + (24 * 3600)
    elif rtime == 0:
        rtime = 24 * 3600
    else:
        pass
    hh = rtime // 3600
    mm = (rtime % 3600) // 60
    ss = (rtime % 3600) % 60

    hh = '%02d' %hh
    mm = '%02d' %mm
    ss = '%02d' %ss
    resttime = hh + ':' + mm + ':' + ss
    return resttime

print(resttime())
#resttime = (lambda x : '0' + x if len(x) < 8 else x)(str(datetime.timedelta(seconds= rtime)))
#print(resttime)

