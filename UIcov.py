import pygame
import json

with open ('datacov.json','r') as file :
    boardgame = json.load(file)[0]

pygame.init()
pygame.display.set_caption("Let's play")
WIDTH = 1536
HEIGHT = 864

def get_font(size):
    return pygame.font.SysFont("8-bit Madness",size)

display = pygame.display.set_mode((WIDTH, HEIGHT),pygame.FULLSCREEN)

def find_gamename(typing) :
    if typing == '' :
        return []
    typing = typing.upper()
    matchname = []
    for i in boardgame :
        i.replace('\u00e9','e')
        if typing in i[:len(typing)].upper() :
            matchname.append(i)

    if len(matchname) < 10 :
        for i in boardgame :
            if typing in i.upper() and i not in matchname:
                matchname.append(i)
                
    if len(matchname) < 10 :
        for i in boardgame :
            for j in typing :
                if j not in list(i.upper()) : break
            if j not in list(i.upper()) : continue
            matchname.append(i)

    while len(matchname) > 10 :
        matchname.pop()
    return matchname

def main():
    clock = pygame.time.Clock()
    findgame = ''
    running = True

    while running:
        display.fill('#ffffff')
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
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

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()
    exit()

if __name__ == "__main__":
    main()

    
