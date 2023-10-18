import pygame
import json
from recommendedgame import *

with open ('datacov.json','r') as file :
    boardgame = json.load(file)[0]

pygame.init()
pygame.display.set_caption("Let's play")
WIDTH = 1536
HEIGHT = 864

display = pygame.display.set_mode((WIDTH, HEIGHT),pygame.FULLSCREEN)

def get_font(size):
    return pygame.font.SysFont("8-bit Madness",size)

def recap(i) :
    a = str(i.replace('\u00e9','e'))
    a = a.replace('\u00e4','a')
    a = a.replace('\u00f9','u')
    a = a.replace('\u014d','o')
    return a

def find_gamename(typing) :
    if typing == '' :
        return []
    typing = typing.upper()
    matchname = []
    for i in boardgame :
        a = recap(i)
        if typing in a[:len(typing)].upper() :
            matchname.append(i)

    if len(matchname) < 10 :
        for i in boardgame :
            a = recap(i)
            if typing in a.upper() and i not in matchname:
                matchname.append(i)
                
    if len(matchname) < 10 :
        for i in boardgame :
            a = recap(i)
            for j in typing :
                if j not in list(a.upper()) : break
            if j not in list(a.upper()) : continue
            if i not in matchname : matchname.append(i)

    while len(matchname) > 10 :
        matchname.pop()
    return matchname

def main():
    clock = pygame.time.Clock()
    findgame = ''
    selectgame = ''
    showselect = False
    running = True

    while running:
        display.fill('#ffffff')

        for event in pygame.event.get() :
            if event.type == pygame.QUIT :
                running = False
            elif event.type == pygame.KEYDOWN :
                if event.key == pygame.K_ESCAPE :
                    running = False

            if event.type == pygame.KEYDOWN:
                showselect = False
                if event.key == pygame.K_BACKSPACE :
                    findgame = findgame[:-1]
                else :
                    findgame += event.unicode

        pygame.draw.rect(display, '#000000', (410, 150, 900, 90), 1)
        type = get_font(100).render(f'Find :  {findgame}', True, '#000000')
        display.blit(type, (200, 160))
            
        match = find_gamename(findgame)
        for i in range(len(match)) :
            type = get_font(50).render(f'{match[i]}', True, '#000000')
            display.blit(type, (200, 270+50*i))
            if pygame.mouse.get_pressed()[0] :
                x,y = pygame.mouse.get_pos()
                if 200 <= x <= 200 + type.get_width() and 270+50*i <= y <= 270+50*i+type.get_height():
                    selectgame = match[i]
                    showselect = False
                    findgame = ''

        if findgame == '' and selectgame != '' : showselect = True
        if showselect :
            type = get_font(57).render(f'{selectgame}', showselect, '#000000')
            display.blit(type, (WIDTH/2-type.get_width()/2,280))
            type = get_font(50).render('if you like this game you must try', showselect, '#000000')
            display.blit(type, (WIDTH/2-type.get_width()/2,330))
            rec = recommend(selectgame)
            for i in range(len(rec)) :  
                type = get_font(50).render(rec[i], showselect, '#000000')
                display.blit(type, (200,400+50*i))

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()
    exit()

if __name__ == "__main__":
    main()

    
