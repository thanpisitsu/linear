import json
import math

with open('databoardgame.json', 'r') as file :
    datasheet = json.load(file)

style = input('Style : ')
player = int(input('Players : '))
weight = int(input('Weight : '))
time = int(input('playTime : '))
weight = weight*50

boardgame = []
for i in datasheet :
    if style == i['Type'] and int(i['Minplayer']) <= player <= int(i['Maxplayer']) :
        boardgame.append(i)

presentboardgame = []

for i in boardgame :
    u0,v0 = weight,int(i['Weight'])
    u1,v1 = time,int(i['Time'])
    # udotv = u0*u1+v0*v1
    # sizeu = math.sqrt(u0**2+v0**2)
    # sizev = math.sqrt(u1**2+v1**2)
    # cosine = math.acos(udotv/sizeu/sizev)
    euclidean = math.sqrt((u0-v0)**2+(u1-v1)**2)
    i['Euclidean'] = euclidean
    presentboardgame.append(i)

presentboardgame.sort(key=lambda t: t['Euclidean'])
while len(presentboardgame) > 10 :
    presentboardgame.pop()

for i in presentboardgame :
    print(i['Name'])