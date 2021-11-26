# import libraries
import pygame
import sys
import os
import random
import time

# Initilize pygame
pygame.init()
pygame.mixer.init()

# Creating game window and change icon
screen_width = 600
screen_height = 500
GameWindow = pygame.display.set_mode((screen_width,screen_height))

# set caption with new icon
pygame.display.set_caption("CAR GAME")
Icon = pygame.image.load("racing-car.png")
pygame.display.set_icon(Icon)
pygame.display.update()

# Loading backgrounds

# MAIN PLAY GROUND
GamebgImg = pygame.image.load("paths.jpg")
GamebgImg = pygame.transform.scale(GamebgImg,(screen_width,screen_height+1000)).convert_alpha()

# PLAYER
carplayer = pygame.image.load("carplayer.jpg")
carplayer = pygame.transform.scale(carplayer,(64,74)).convert_alpha()

# intro-section
introImg = pygame.image.load("home_page.jpeg")
introImg = pygame.transform.scale(introImg,(screen_width,screen_height)).convert_alpha()

# instruction-page
instrImg = pygame.image.load("intruction.jpeg")
instrImg = pygame.transform.scale(instrImg,(screen_width,screen_height)).convert_alpha()

# paused-screen
pauseImg = pygame.image.load("puased.png")
pauseImg = pygame.transform.scale(pauseImg,(screen_width,screen_height)).convert_alpha()

# crashed-screen
crashImg = pygame.image.load("crashed.jpeg")
crashImg = pygame.transform.scale(crashImg,(screen_width,screen_height)).convert_alpha()

# Colors-RGB
white = (255,255,255)
red = (255,45,0)
light_red =(200,0,0)
green = (166,161,142)
light_green = (166,141,122)
blue = (0,81,236)
light_blue =(0,0,200)
black = (0,0,0)
blr = (0,121,152)
light_blr = (60,214,230)
radis = (195,54,44)
light_radis = (170,50,40)

# clock
clock = pygame.time.Clock()
fps = 82

# BLIT ENEMY CARS ON TOP OF SCREEN
def carBlits(randcar,pathx,pathy):
    car = pygame.image.load("9.png")
    car = pygame.transform.scale(car, (65, 65)).convert_alpha()
    if randcar == 0:
        car = pygame.image.load("9.png")
        car = pygame.transform.scale(car,(65,65)).convert_alpha()
      
    elif randcar == 1:
        car = pygame.image.load("1.png")
        car = pygame.transform.scale(car, (65,65)).convert_alpha()

    elif randcar == 2:
        car = pygame.image.load("2.png")
        car = pygame.transform.scale(car, (65,65)).convert_alpha()

    elif randcar == 3:
        car = pygame.image.load("3.png")
        car = pygame.transform.scale(car, (65,65)).convert_alpha()

    elif randcar == 4:
        car = pygame.image.load("4.png")
        car = pygame.transform.scale(car, (65,65)).convert_alpha()

    elif randcar == 5:
        car = pygame.image.load("5.png")
        car = pygame.transform.scale(car, (65,65)).convert_alpha()

    elif randcar == 6:
        car = pygame.image.load("7.png")
        car = pygame.transform.scale(car, (65,65)).convert_alpha()

    elif randcar == 7:
        car = pygame.image.load("8.png")
        car = pygame.transform.scale(car, (65,65)).convert_alpha()

    elif randcar == 8:
        car = pygame.image.load("10.png")
        car = pygame.transform.scale(car, (65,65)).convert_alpha()

    GameWindow.blit(car, (pathx, pathy))

# fxn to show instruction page
def intstruction():
    instr = True
    while instr:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                sys.exit()
        # set background image for instruction page
        GameWindow.blit(instrImg,(0,0))

        # message for user
        font = pygame.font.Font("freesansbold.ttf",30)
        text = font.render("HOW TO PLAY ?",True,black)

        font = pygame.font.Font("freesansbold.ttf", 20)
        i1 = font.render("-> for Move car right",True,white)
        i2 = font.render("<- for Move car left",True,white)
        i3 = font.render("a for  car Accleration",True,white)
        i4 = font.render("b for  car Brake",True,white)

        GameWindow.blit(text,(100,20))
        GameWindow.blit(i1, (100, 80))
        GameWindow.blit(i2, (100, 120))
        GameWindow.blit(i3, (100, 160))
        GameWindow.blit(i4, (100, 200))

        # Button-Back btn
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        if mouse[0]>100 and mouse[0]<200 and mouse[1]>300 and mouse[1]<350:
            pygame.draw.rect(GameWindow, blr , (100, 300, 100, 50))
            if click == (1,0,0):
                intro_page()
        else:
            pygame.draw.rect(GameWindow, light_blr, (100, 300, 100, 50))

        font = pygame.font.Font("freesansbold.ttf", 30)
        bt_text = font.render("BACK",True,black)
        GameWindow.blit(bt_text,(107,310))

        pygame.display.update()
        clock.tick(fps)

# fxn for intro page of game
def intro_page():
    intro = True
    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    Game_loop()
        # set intro page background image
        GameWindow.blit(introImg, (0, 0))

        # for Buttons
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        # start-btn
        if mouse[0]>50 and mouse[0]<150 and mouse[1]>400 and mouse[1]<450:
            pygame.draw.rect(GameWindow,light_blue,(50,400,100,50))
            if click == (1,0,0):
                Game_loop()
        else:
            pygame.draw.rect(GameWindow, blue, (50, 400, 100, 50))

        font = pygame.font.Font("freesansbold.ttf", 20)
        text = font.render("START", True, black)
        GameWindow.blit(text, (70, 415))

        # instruction-btn
        if mouse[0]>250 and mouse[0]<350 and mouse[1]>400 and mouse[1]<450:
            pygame.draw.rect(GameWindow,light_green,(250,400,100,50))
            if click == (1,0,0):
                intstruction()
        else:
            pygame.draw.rect(GameWindow, green, (250, 400, 100, 50))

        font = pygame.font.Font("freesansbold.ttf", 20)
        text = font.render("HELP", True, black)
        GameWindow.blit(text, (270, 415))

        # quit-btn
        if mouse[0]>450 and mouse[0]<550 and mouse[1]>400 and mouse[1]<450:
            pygame.draw.rect(GameWindow,light_red,(450,400,100,50))
            if click == (1,0,0):
                pygame.quit()
                quit()
                sys.exit()
        else:
            pygame.draw.rect(GameWindow, red, (450, 400, 100, 50))

        font = pygame.font.Font("freesansbold.ttf", 20)
        text = font.render("QUIT", True, black)
        GameWindow.blit(text, (470, 415))
        pygame.display.update()
        clock.tick(fps)

# fxn for scr show when game paused
def paused():
    puase = True
    while puase:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                sys.exit()
        GameWindow.blit(pauseImg,(0,0))

        # buttons
        font = pygame.font.Font("freesansbold.ttf", 20)
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        # Continue-btn
        if mouse[0]>100 and mouse[0]<220 and mouse[1]>400 and mouse[1]<450:
            pygame.draw.rect(GameWindow, blue, (100, 400, 120, 50))
            if click == (1,0,0):
                puase = False
        else:
            pygame.draw.rect(GameWindow, light_blue, (100, 400, 120, 50))
        cont = font.render("CONTINUE",True,white)
        GameWindow.blit(cont,(105,415))

        # Main_menu-btn
        if mouse[0]>370 and mouse[0]<490 and mouse[1]>400 and mouse[1]<450:
            pygame.draw.rect(GameWindow, red, (370, 400, 120, 50))
            if click == (1,0,0):
                intro_page()
        else:
            pygame.draw.rect(GameWindow, light_red, (370, 400, 120, 50))
        main_menu = font.render("MAIN MENU", True, white)
        GameWindow.blit(main_menu, (370, 420))

        pygame.display.update()
        clock.tick(32)

# fxn for scr show when crashing occurs with player and another enemy car
def crashed(flag,new_high_score):
    crash = True
    while crash:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                sys.exit()
        GameWindow.blit(crashImg,(0,0))

        # buttons

        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        # Restart
        if mouse[0]>100 and mouse[0]<250 and mouse[1]>200 and mouse[1]<250:
            pygame.draw.rect(GameWindow,green,(100,200,150,50))
            if click == (1,0,0):
                Game_loop()
        else:
            pygame.draw.rect(GameWindow, light_green, (100, 200, 150, 50))

        font = pygame.font.Font("freesansbold.ttf",20)
        restart = font.render("RESTART",True,black)
        GameWindow.blit(restart,(120,220))

        # Main menu
        if mouse[0] > 100 and mouse[0] < 250 and mouse[1] > 300 and mouse[1] < 350:
            pygame.draw.rect(GameWindow, red, (100, 300, 150, 50))
            if click == (1,0,0):
                intro_page()
        else:
            pygame.draw.rect(GameWindow, light_red, (100, 300, 150, 50))
        Main_menu = font.render("MAIN MENU", True, black)
        GameWindow.blit(Main_menu, (115, 320))

        if not flag:
            new = font.render("New High score : "+str(new_high_score),True,white)
            GameWindow.blit(new,(100,100))

        pygame.display.update()
        clock.tick(32)

# Main Game logic is here only
# Game Loop
def Game_loop():

    # Game variables
    game_exit = False
    game_over = False
    carX = 280
    carY = 400
    car_vel_x = 0
    car_vel_y = 0
    car_movex = 4
    car_movey = 2

    bgx = 0
    bgy = -600
    bg_yvel = 10

    # ENEMY CAR PARAMETER
    pathx = random.randint(100, screen_width - 100)
    pathy = random.randint(0, 10)

    randcar = 0
    path_Yvel = 5

    # score
    score = 0
    level = 0

    # highscore
    ''' High score'''
    # check if file not exit
    if (not os.path.exists("highscore.txt")):
        with open("highscore.txt", "w") as file:
            file.write("0")
    with open("highscore.txt", "r") as file:
        his_score = file.read()

    while not game_exit:

        # event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_exit = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    car_vel_x = car_movex
                if event.key == pygame.K_LEFT:
                    car_vel_x = -car_movex
                if event.key == pygame.K_UP:
                    car_vel_y = 0
                if event.key == pygame.K_DOWN:
                    car_vel_y = 0
                if event.key == pygame.K_a:
                    path_Yvel += 1
                if event.key == pygame.K_b:
                    if path_Yvel>=5:
                        path_Yvel -= 1
            if event.type == pygame.KEYUP:
                car_vel_x = 0
                car_vel_y = 0


        carX += car_vel_x
        carY += car_vel_y
        bgy += bg_yvel
        if bgy>-30:
            bgy = -600

        GameWindow.blit(GamebgImg, (bgx, bgy))
        GameWindow.blit(carplayer,(carX,carY))

        pathy += path_Yvel

        # crashed
        if  carX<50 :
            carX=50
            carY=400
        if carX+64>screen_width-50:
            carX = screen_width-50-64
            carY = 400
        if pathy > 400-65:
            if carX<pathx+65<carX+64 or pathx+65>carX+64>pathx :
                # update score if new high score
                flag = True
                if score > int(his_score):
                    flag = False
                    his_score = str(score)
                    with open("highscore.txt", "w") as file:
                        file.write(his_score)
                    font = pygame.font.Font("freesansbold.ttf", 15)
                    high_score = font.render("High-score : "+his_score,True,white)
                    GameWindow.blit(high_score,(240,480))

                font = pygame.font.Font("freesansbold.ttf",45)
                game_crashed = font.render("CRASHED",True,white)
                GameWindow.blit(game_crashed,(200,screen_height/2))
                pathy = random.randint(0, 10)
                pygame.display.update()
                time.sleep(2)
                new_high_score = int(his_score)
                crashed(flag,new_high_score)

        if pathy>500:
            pathx = random.randint(100, screen_width - 100)
            pathy = random.randint(0, 10)
            randcar = random.randint(0,9)

            # update score
            score += 1
            if score % 10 == 0:
                level += 1
                path_Yvel += 1
                if level % 10 == 0 and bg_yvel<=15:
                    bg_yvel += 1
        font = pygame.font.Font("freesansbold.ttf", 15)
        score_text = font.render("score : " + str(score), True, white)
        level_show = font.render("level : " + str(level), True, white)
        GameWindow.blit(score_text, (270, 480))
        GameWindow.blit(level_show, (0, 480))

        carBlits(randcar,pathx,pathy)

        #  Puase button
        font = pygame.font.Font("freesansbold.ttf", 15)
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        if mouse[0] > 550 and mouse[0] < 600 and mouse[1] > 0 and mouse[1] < 100:
            pygame.draw.rect(GameWindow,white,(550,0,100,50))
            if click == (1, 0, 0):
                paused()
        else:
            pygame.draw.rect(GameWindow,white,(550,0,100,50))

        pause = font.render("PAUSE", True, radis)
        GameWindow.blit(pause,(550,20))

        pygame.display.update()
        clock.tick(fps)

    pygame.quit()
    quit()
intro_page()
Game_loop()