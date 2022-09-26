"""

seasonnum = int(input())
snum = seasonnum//3
print(snum)
season = str()

if snum == 1:
    season == 'spring'
elif snum == 2:
    season == 'summner'
elif snum == 3:
    season == 'fall'
else:
    season == 'winter'

print(season)
"""
snumshare = int(input())//3
season = ''
def findseason():
    if snumshare == 1:
        season = 'spring'
    elif snumshare == 2:
        season = 'summer'
    elif snumshare == 3:
        season = 'fall'
    else:
        season = 'winter'
    print(season)

findseason()
