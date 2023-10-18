import pygame
from  searchgame import *

pygame.init()
pygame.display.set_caption("Let's play")
WIDTH = 1536
HEIGHT = 864

def get_font(size):
    return pygame.font.SysFont("8-bit Madness",size)

display = pygame.display.set_mode((WIDTH, HEIGHT),pygame.FULLSCREEN)
menu_items = ["strategygames", "thematic", "wargames",'cgs','abstracts','familygamess','partygames','childrensgames','cancel']
gametype = ''
dropstart = 320
clicking = ''

def draw_dropdown():
    pygame.draw.rect(display, '#ffffff', (dropstart, 370, 250, 40))
    pygame.draw.rect(display, '#000000', (dropstart, 370, 250, 40), 1)
    type = get_font(30).render('Type', True, '#000000')
    display.blit(type, (150, 380))
    if gametype:
        text = get_font(30).render(gametype, True, '#000000')
        display.blit(text, (dropstart+10, 380))
    else:
        text = get_font(30).render("Select option", True, '#000000')
        display.blit(text, (dropstart+10, 380))

def draw_menu():
    for i, item in enumerate(menu_items):
        y = 410 + (i * 40)
        pygame.draw.rect(display, '#ffffff', (dropstart, y, 250, 40))
        pygame.draw.rect(display, '#000000', (dropstart, y, 250, 40), 1)
        text = get_font(30).render(item, True, '#000000')
        if i == len(menu_items)-1 : text = get_font(30).render(item, True, '#ff0000')
        display.blit(text, (dropstart +10, y + 10))

def draw_numplay(num) :
    pygame.draw.rect(display, '#ffffff', (dropstart, 100, 250, 40))
    pygame.draw.rect(display, '#000000', (dropstart, 100, 250, 40), 1)
    type = get_font(30).render('Players', True, '#000000')
    display.blit(type, (150, 110))
    if clicking=='num' or num != '' :
        text = get_font(30).render(num, True, '#000000')
        display.blit(text, (dropstart+10, 110))

def draw_weight(weight) :
    pygame.draw.rect(display, '#ffffff', (dropstart, 190, 250, 40))
    pygame.draw.rect(display, '#000000', (dropstart, 190, 250, 40), 1)
    type = get_font(30).render('Weight (1-10)', True, '#000000')
    display.blit(type, (150, 200))
    recommended = get_font(22).render('if you never play boardgame we recommended weight 1-3', True, '#000000')
    display.blit(recommended, (150, 235))
    if clicking=='num' or weight != '' :
        text = get_font(30).render(weight, True, '#000000')
        display.blit(text, (dropstart+10, 200))

def draw_time(time) :
    pygame.draw.rect(display, '#ffffff', (dropstart, 280, 250, 40))
    pygame.draw.rect(display, '#000000', (dropstart, 280, 250, 40), 1)
    type = get_font(30).render('Time (minutes)', True, '#000000')
    display.blit(type, (150, 290))
    if clicking=='time' or time != '' :
        text = get_font(30).render(time, True, '#000000')
        display.blit(text, (dropstart+10, 290))

def show_boardgame(boardgames):
    for i in range(len(boardgames)):
        name = get_font(30).render(f'{i+1}    {boardgames[i]["Name"]}', True, '#000000')
        display.blit(name, (700, 100+i*70))
        detail = get_font(25).render(f'Type : {boardgames[i]["Type"]}  Weight : {int(boardgames[i]["Weight"])/50}  Players : {boardgames[i]["Minplayer"]} - {boardgames[i]["Maxplayer"]}  Playtime : {boardgames[i]["Time"]} ', True, '#000000')
        display.blit(detail, (720, 125+i*70))


def main():
    global gametype
    global clicking

    clock = pygame.time.Clock()

    running = True
    menu_open = False
    numplay = ''
    weight = ''
    time = ''
    boardgames = []

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                if 300 <= event.pos[0] <= 490 and 370 <= event.pos[1] <= 410:
                    menu_open = not menu_open
                elif menu_open and 300 <= event.pos[0] <= 490:
                    item_index = (event.pos[1] - 410) // 40
                    if 0 <= item_index < len(menu_items)-1:
                        gametype = menu_items[item_index]
                        menu_open = False
                    else :
                        menu_open = False
                        gametype = ''

                elif 300 <= event.pos[0] <= 490 and 100 <= event.pos[1] <= 140:
                    clicking = 'num'
                elif 300 <= event.pos[0] <= 490 and 190 <= event.pos[1] <= 230:
                    clicking = 'weight'
                elif 300 <= event.pos[0] <= 490 and 280 <= event.pos[1] <= 320:
                    clicking = 'time'
                elif 150 <= event.pos[0] <= 240 and 470 <= event.pos[1] <= 510:
                    boardgames = find_boardgame(numplay,weight,time,gametype)

            if event.type == pygame.KEYDOWN:
                if clicking == 'num' :
                    if event.key == pygame.K_BACKSPACE:
                            numplay = numplay[:-1]
                    elif len(numplay) < 3:
                        if event.unicode.isdigit():
                            numplay += event.unicode

                elif clicking == 'weight' :
                    if event.key == pygame.K_BACKSPACE:
                            weight = weight[:-1]
                    elif len(weight) == 1 and weight == '1' and event.unicode == '0':
                            weight += '0'
                    elif len(weight) < 1 and event.unicode.isdigit() and event.unicode != '0':
                        weight += event.unicode

                elif clicking == 'time' :
                    if event.key == pygame.K_BACKSPACE:
                            time = time[:-1]
                    elif len(time) < 4:
                        if event.unicode.isdigit():
                            time += event.unicode

        display.fill('#ffffff')

        pygame.draw.rect(display, '#ffffff', (150, 470, 90, 40))
        pygame.draw.rect(display, '#000000', (150, 470, 90, 40), 1)
        type = get_font(30).render('Search', True, '#000000')
        display.blit(type, (160, 480))

        draw_time(time)
        draw_numplay(numplay)
        draw_weight(weight)
        draw_dropdown()
        if menu_open:
            draw_menu()
        show_boardgame(boardgames)

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()
    exit()

if __name__ == "__main__":
    main()

    