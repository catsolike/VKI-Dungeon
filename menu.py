import pygame as pg
import pygame
from PIL import Image
from pygame import font

def menu():
    import sys
    pygame.init()
    pygame.display.set_caption('ВКИ Dungeon')

    screen_size = Image.open('menu_background.png')
    screenX, screenY = screen_size.size
    screen = pygame.display.set_mode([screenX, screenY])

    background = pygame.image.load('menu_background.png')
    screen.blit(background,(0, 0))

    text_color = [240, 250, 255]
    menu_text = 'ВКИ Dungeon'
    font = pygame.font.Font('progresspixel.ttf', 40)
    text = font.render (menu_text, 1, text_color)
    screen.blit(text, [20, 0])

    item_bg = pygame.image.load('item_bg.png')
    item_color = [255, 0, 50]
    item_size = Image.open('item_bg.png')
    item_width, item_height = item_size.size
    item_font = pygame.font.Font('progresspixel.ttf', 30)
    item_x = screenX - item_width - 10

    text_item = ["Play", 'Help', "Exit"]
    n = len(text_item)

    item_y = [0]*n
    for i in range(n):
        item_y[i] = 100*(i+1)

    color = (200, 0, 0)

    menu_running = True
    while menu_running:
        for i in range(n):
            screen.blit(item_bg, [item_x, item_y[i]])
            text = item_font.render(text_item[i], 1, text_color)
            screen.blit(text, [item_x + item_width//3, item_y[i]+10])
        
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                menu_running = False
                
            if event.type == pygame.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    pygame.quit()
                if event.key == pg.K_RETURN: #Клавиша Enter
                    import game
                    game.main()
                
                            
            if event.type == pg.MOUSEBUTTONDOWN:
                (xm, ym) = pg.mouse.get_pos()

                for i in range(n):
                    if xm >= item_x and xm <= item_x + item_width and ym >= item_y[i] and ym <= item_y[i] + item_height:
                        if i == 0:
                            import game
                            game.main()
                            
                        if i == 1:
                            help()                           
                            
                        if i == n-1:
                            pg.quit()
    pygame.quit()

def help():
    pg.init()

    screen_size = Image.open('menu_background.png')
    screenX, screenY = screen_size.size
    screen = pygame.display.set_mode([screenX, screenY])

    #Загрузка изображений
    background = pg.image.load('menu_background.png')
    live = pg.image.load('live.png')
    enemy = pg.image.load('enemy.png')
    door_ex = pg.image.load('door_ex.png')
    money = pg.image.load('money.png')
    screen.blit(background, [0, 0])
    
    cs = 40
    
    txt = ['Управление осуществляется стрелками.', 'Иногда тебе нужно будет', 'использовать и другие клавиши.','','Это твое здоровье. Держи его выше нуля.','', 'Это твой враг.','', 'Это сокровища.','', 'Это спуск в глубины подземелья']
    clen = len(txt)
    
    text_color = [200, 0, 0]
    font = pygame.font.Font('progresspixel.ttf', 28)
    for i in range(clen):
        text = font.render(txt[i], 1, text_color)
        screen.blit(text, [2*cs+10, (i+1)*cs])
        
    expos = ['Искатель приключений исследует темные лабиринты Подземелья ВКИ в поисках сокровищ.','Иногда он встречает врагов.',' Сможет ли он победить всех и дойти до конца?', 'Разработчик Киселелев Данил дмитриевич, группа 007Б2']
    elen = len(expos)

    text_color = ([20, 20, 20])
    font = pygame.font.Font('progresspixel.ttf', 20)
    for i in range(elen):
        text = font.render(expos[i], 1, text_color)
        screen.blit(text, [20, (i+12)*cs])

    screen.blit(live, [20, 5*cs])
    screen.blit(enemy, [20, 7*cs])
    screen.blit(money, [20, 9*cs])
    screen.blit(door_ex, [20, 11*cs])

def intro_fun():
    pg.init()
    pygame.display.set_caption('ВКИ Dungeon')
    pg.time.set_timer(pg.USEREVENT, 75)
    
    intro = ['Intro 0.png', 'Intro 1.png', 'Intro 3.png', 'Intro 4.png', 'Intro 5.png']
    intro_len = len(intro)

    intro_anim = [0]*intro_len
    for i in range(intro_len):
        intro_anim[i] = pg.image.load(intro[i])
    
    screenX = 1200
    screenY = 640
    screen = pygame.display.set_mode([screenX, screenY])
    screen.fill([45, 40, 43])

    text_color = [240, 250, 255]
    intro_text = 'Нажмите любую клавишу, чтобы продолжить'
    font = pygame.font.Font('progresspixel.ttf', 20)
    text = font.render (intro_text, 1, text_color)
    screen.blit(text, [320, 500])

    frame = 0
    
    intro_process = True
    while intro_process:
        pg.display.flip()

        for event in pg.event.get():
            if event.type == pg.USEREVENT:
                if frame < intro_len:
                    screen.blit(intro_anim[frame], [536, 256])
                    frame += 1
                else:
                    frame = 0
            
            if event.type == pg.KEYDOWN:
                kd = pg.key.name(event.key)
                if kd != 'escape':
                    menu()
                if kd == 'escape':
                    pygame.quit()
            if event.type == pygame.QUIT:
                pygame.quit()
