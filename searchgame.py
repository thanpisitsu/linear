import json
import math

with open('databoardgame.json', 'r') as file :
    datasheet = json.load(file)

def find_boardgame(player,weight,time,style) :
    boardgame = []
    for i in datasheet :
        if style == '' and int(i['Minplayer']) <= int(player) <= int(i['Maxplayer']) :
            boardgame.append(i)
        elif style == i['Type'] :
            if player == '' :
                boardgame.append(i)
            if int(i['Minplayer']) <= int(player) <= int(i['Maxplayer']) :
                boardgame.append(i)

    presentboardgame = []

    for i in boardgame :
        weight = int(i['Weight']) if weight == '' else int(weight)*50
        time = int(i['Time']) if time == '' else int(time)
        u0,v0 = weight,int(i['Weight'])
        u1,v1 = time,int(i['Time'])
        # udotv = u0*u1+v0*v1
        # sizeu = math.sqrt(u0**2+v0**2)
        # sizev = math.sqrt(u1**2+v1**2)
        # cosine = math.acos(udotv/sizeu/sizev)
        a = (u0-v0)**2+(u1-v1)**2
        if a < 10000 :
            euclidean = math.sqrt(a)
            i['Euclidean'] = euclidean
        else :
            i['Euclidean'] = 1000.0
        presentboardgame.append(i)

    presentboardgame.sort(key=lambda t: t['Euclidean'])
    while len(presentboardgame) > 10 :
        presentboardgame.pop()
    return presentboardgame