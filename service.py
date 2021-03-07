import pickle
import pygame as pg
import pygame
from pygame import font

player_nick = ''

def naming():
    pygame.init()
    pygame.display.set_caption("ВКИ Dungeon. Введите ник")

    global player_nick 
    
    screen = pygame.display.set_mode([1200, 640])
    screen.fill([45, 40, 43])
    
    text_color = ([240, 250, 255])
    font = pg.font.Font('progresspixel.ttf', 20)
    text = font.render('Введите свой ник:', 0, text_color)
    screen.blit(text, [120, 80])
        
    nicknaming = ''
    def nick_inp(nicknaming):
        global player_nick
        txt_bg_color = ([45, 40, 43])
        text_color = ([250, 250, 100])  

        kd = pg.key.name(event.key)
        if kd != 'return' and kd != 'backspace' and kd != 'escape' and kd != 'left' and kd != 'right' and kd != 'up' and kd != 'down':
            nicknaming = nicknaming + kd
            
        if kd == 'return':
            player_nick = nicknaming
            text = font.render('Принято!', 0, ([240, 250, 255]))
            pg.draw.rect(screen, txt_bg_color, [120, 160, 1200, 40], 0)
            screen.blit(text, [120, 160])
        if kd == 'backspace':
            kd = ''
            a = len(nicknaming)-1
            nicknaming = nicknaming[0:a]

        if kd == 'escape':
            pg.quit()

        inp_text = font.render(nicknaming, 0, text_color)
        pg.draw.rect(screen, txt_bg_color, [160, 120, 1200, 40], 0)
        screen.blit(inp_text, [160, 120])
        
        return(nicknaming)
            
    nick_input = True
    while nick_input:
        for event in pg.event.get():
            if event.type == pg.KEYDOWN:
                nicknaming = nick_inp(nicknaming)
                
        pg.display.flip()

##def recording():
##    nicks=["Пусто", "Пусто", "Пусто", "Пусто", "Пусто", 0, 0, 0, 0, 0,]
##    pickle_file = open('records.txt', 'wb')#открытие файла для записи
##    pickle.dump(nicks, pickle_file)
##    pickle_file.close()
