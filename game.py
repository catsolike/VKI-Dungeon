level_counter = 0 #level counter счетчик уровней
counter = level_counter
score = 0
def main():
    global level_counter 
    global counter
    global score
    import service
    import menu
    import random
    import pygame as pg
    import pygame
    pg.init()
    from pygame import font
    pg.time.set_timer(pg.USEREVENT, 1000)

    game_name = 'ВКИ Dungeon'
    pg.display.set_caption(game_name)

    levels = ['level_1.txt', 'level_2.txt', 'level_3.txt']
    level_quality = len(levels)

    timer = 5
    cs = 40 
    
    #создание матрицы для карты уровня
    cells = 16
    lvl = [0]*cells
    for i in range(cells):
        lvl[i] = [0]*cells
    lvl_file = open(levels[level_counter], 'r')
    
    for i in range(cells):
        strings = lvl_file.readline() 
        clean = strings.split() 
        for j in range(cells):
            lvl[i][j] = int(clean[j])
##    lvl_file.close()

    darkness = [1]*cells #создание препятсвия для глаз поверх лабиринта, чтобы игрок не мог сразу узнать, куда ему идти, а исследовал уровень
    for i in range(cells):
        darkness[i] = [1]*cells
    
    player = pg.image.load('player.png') 
    wall = pg.image.load('wall.png')
    floor = pg.image.load('floor.png')
    exit_lvl = pg.image.load('door_ex.png')
    money = pg.image.load('money.png')
    dark = pg.image.load('dark.png')
    enemy = pg.image.load('enemy.png')
    game_bg = pg.image.load('game_bg.jpg')
    live = pg.image.load('live.png')
    
    screenX = 1200
    screenS = cs*cells
    screen = pg.display.set_mode((screenX, screenS))
    screen.blit(game_bg, [0, 0])

    text_color = [240, 250, 255]
    txt_bg_color = [45, 40, 43]
    font = pg.font.Font('progresspixel.ttf', 20)
    pg.draw.rect(screen, txt_bg_color, [screenS+cs, cs, screenX - screenS - 2*cs, screenS - 2*cs])
    
    def draw_map(): #рисование уровня
        for i in range(cells):
            for j in range(cells):
                x = cs*j
                y = cs*i
                if lvl[i][j] == 6: #игрок
                    screen.blit(floor, [x, y])
                    screen.blit(player, [x, y])
                    ip = i 
                    jp = j

                    darkness[i][j] = lvl[i][j] #в области, близкой к игроку препятствие для глаз исчезает
                    darkness[i+1][j] = lvl[i+1][j]
                    darkness[i-1][j] = lvl[i-1][j]
                    darkness[i][j+1] = lvl[i][j+1]
                    darkness[i][j-1] = lvl[i][j-1]
                    darkness[i+1][j-1] = lvl[i+1][j-1]
                    darkness[i-1][j+1] = lvl[i-1][j+1]
                    darkness[i-1][j-1] = lvl[i-1][j-1]
                    darkness[i+1][j+1] = lvl[i+1][j+1]
                    
                    if i+2 < cells: #чтобы игрок изначально знал, что впереди враг или выход с уровня
                        if (lvl[i+2][j] == 3 or lvl[i+2][j] == 10) and lvl[i+1][j] != 0: 
                            darkness[i+2][j] = lvl[i+2][j]
                        if (lvl[i-2][j] == 3 or lvl[i-2][j] == 10) and lvl[i-1][j] != 0:
                            darkness[i-2][j] = lvl[i-2][j]
                    if j+2 < cells:        
                        if (lvl[i][j+2] == 3 or lvl[i][j+2] == 10) and lvl[i][j+1] != 0:
                            darkness[i][j+2] = lvl[i][j+1]
                        if (lvl[i][j-2] == 3 or lvl[i][j-2] == 10) and lvl[i][j-1] != 0:
                            darkness[i][j-2] = lvl[i][j-2]

                if lvl[i][j] == 0:              #стена
                    screen.blit(wall, [x, y])
                elif lvl[i][j] == 2:            #пол
                    screen.blit(floor, [x, y])
                elif lvl[i][j] == 3:            #выход с уровня
                    screen.blit(exit_lvl, [x, y])
                elif lvl[i][j] == 5:            #игровые очки
                    screen.blit(floor, [x, y])
                    screen.blit(money, [x, y])
                elif lvl[i][j] == 10:           #враг
                    screen.blit(floor, [x, y])
                    screen.blit(enemy, [x, y])
                    
                if darkness[i][j] == 1:         #препятсвие для глаз
                    screen.blit(dark, [x, y])
        return(ip, jp)
    
    def control(i, j, ip, jp):          #передвижение игрока
        if event.key == pg.K_UP:
            i = ip - 1
        elif event.key == pg.K_DOWN:
            i = ip + 1
        elif event.key == pg.K_LEFT:
            j = jp - 1
        elif event.key == pg.K_RIGHT:
            j = jp + 1       
        return(i, j)    

    def moving(i, j, ip, jp, lvl, lives, sp_in, spell_change, spell_result): #передвижение
        global level_counter
        global score
        
        if lvl[i][j] == 0:
            i = ip
            j = jp
            
        if lvl[i][j] == 2:
            lvl[i][j] = 6       #игрок переходит на следующую клетку
            lvl[ip][jp] = 2     #предыдущая клетка закрывается полом
            ip = i
            jp = j
            
        if lvl[i][j] == 5:
            lvl[i][j] = 6
            lvl[ip][jp] = 2
            ip = i
            jp = j          
            score += 1      
            
        if lvl[i][j] == 3: #переход на новый уровень
            level_counter += 1
            lvl[i][j] = 6
            lvl[ip][jp] = 2
            ip = i
            jp = j
            
        if lvl[i][j] == 10:
            lenemy, lives, sp_in, spell_change, spell_result = pve(lives, sp_in, spell_change, spell_result)
            if lenemy <= 0:
                lvl[i][j] = 6
                lvl[ip][jp] = 2
                ip = i
                jp = j
                
        ip, jp = draw_map()
        return(i, j, ip, jp, lvl, lives, sp_in, spell_change, spell_result)

    liters = str('qwertyuiasdfghjklzxcvbnm')
    litq = len(liters)    
    lives = 10
    sp_in = ''
    spell_change = True
    spell_result = ''
    def pve(lives, sp_in, spell_change, spell_result):            #боевая система
        lives_enemy = 1
        spell = ''
        spell_len = random.randint(5, 8)
        
        if spell_change == True and spell_result == '': #предотвращает изменение выводимой на экран комбинации букв, если игрок вводит ее
            for i in range(spell_len):
                f = random.randint(0, litq-1)
                spell += str(liters[f])
            spell_result = spell
        spell_change = False
        
        text = font.render('Введи ' + spell_result + ' на клавиатуре', 0, text_color)
        pg.draw.rect(screen, txt_bg_color, [screenS+2*cs, 6*cs, 10*cs, cs], 0)
        screen.blit(text, [screenS+2*cs, 6*cs])
        inp_text = font.render('', 0, text_color)
        answer = ''

        inp = True
        kd = pg.key.name(event.key)
        if kd == 'return':
           answer = sp_in
           inp = False
           spell_change = True
           
        if kd != 'return' and kd != 'backspace' and kd != 'left' and kd != 'right' and kd != 'up' and kd != 'down':
            sp_in = sp_in + kd
            
        if kd == 'backspace':
            kd = ''
            a = len(sp_in)-1
            sp_in = sp_in[0:a]
            
        inp_text = font.render(sp_in, 0, text_color)
        pg.draw.rect(screen, txt_bg_color, [screenS+2*cs, 7*cs, 10*cs, cs], 0)
        screen.blit(inp_text, [screenS+2*cs, 7*cs])
        pg.draw.rect(screen, txt_bg_color, [screenS+2*cs, 8*cs, 10*cs, cs], 0)
        if inp == False:
            if answer == spell_result:
                lives_enemy -= 1
                spell_result = ''
                sp_in = ''
                text = font.render('Ты изгнал монстра', 0, text_color)
                screen.blit(text, [screenS+2*cs, 8*cs])
                
            elif lives > 0:
                lives -= random.randint(1, 3)
                spell_result = ''
                sp_in = ''
                text = font.render('Монстр ударил тебя', 0, text_color)
                screen.blit(text, [screenS+2*cs, 8*cs])
        
        return(lives_enemy, lives, sp_in, spell_change, spell_result)
    
    ip, jp = draw_map()
    i = ip
    j = jp
    gameprocess = True
    while gameprocess:
        text = font.render ('Сокровища: ' + str(score), 0, text_color)
        pg.draw.rect(screen, txt_bg_color, [screenS+3*cs, 3*cs, 10*cs, cs], 0)
        screen.blit(text, [screenS+3*cs, 3*cs])
        screen.blit(money, [screenS + 10*cs, 3*cs])

        text = font.render('Здоровье: ' + str(lives), 0, text_color)
        pg.draw.rect(screen, txt_bg_color, [screenS+3*cs, 4*cs, 10*cs, cs], 0)
        screen.blit(text, [screenS + 3*cs, 4*cs])
        screen.blit(live, [screenS + 10*cs, 5+4*cs])
        
        if level_counter == counter + 1 and level_counter < level_quality:   #когда счетчик уровней изменяется, программа запускается заново
            counter = level_counter
            gameprocess = False
            
        if level_counter >= level_quality:
            lives = 0
        
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                
            if lives <= 0:
                score = 0
                level_counter = 0
                text = font.render("Game over. Приготовьтесь вводить ник", 0, text_color)
                screen.blit(text, [screenS+cs, 0])
                if event.type == pg.USEREVENT:     
                    timer -= 1
                if timer <= 0:
                    service.naming()
                            
            if event.type == pg.KEYDOWN:
                i, j = control(i, j, ip, jp)
                i, j, ip, jp, lvl, lives, sp_in, spell_change, spell_result = moving(i, j, ip, jp, lvl, lives, sp_in, spell_change, spell_result)
                if event.key == pg.K_ESCAPE:
                    score = 0
                    menu.menu()
        pg.display.flip()

while True:        
    main()
