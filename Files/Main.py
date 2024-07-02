import pygame
import random
import button

pygame.init()

width = 920
height = 620

screen = pygame.display.set_mode((width,height))

clock = pygame.time.Clock()

back = pygame.image.load("Field.png")
ball = pygame.image.load("Football.png")
kepp = pygame.image.load("Player.png")
kepp2 = kepp
imga = pygame.image.load("Controls.png").convert_alpha()
opti = pygame.transform.scale(imga, (width,height))
img = pygame.image.load("Mainmenu.png").convert_alpha()
wall = pygame.transform.scale(img, (width,height))

start = pygame.image.load("start.png").convert_alpha()
option = pygame.image.load("options.png").convert_alpha()
exit_img = pygame.image.load("exit.png").convert_alpha()
back_img = pygame.image.load("back.png").convert_alpha()

start_button = button.Button(358, 280, start, 2)
option_button = button.Button(358, 390, option, 2)
exit_button = button.Button(358, 500, exit_img, 2)
back_button = button.Button(358, 490, back_img, 2)

def run():
    game = True
    
    ballx = 500
    bally = 310
    
    vilx = 5
    vily = 5
    
    n = random.randint(0,1)
    m = random.randint(0,1)
    
    if n==0:
        bal = True
    if n==1:
        bal = False
    
    if m==0:
        baly = True
    if m==1:
        baly = False
    
    keppx = 100
    keppy = 200
    
    kepp2x = 760
    kepp2y = 200
    
    score1 = 0
    score2 = 0
    
    font = pygame.font.SysFont(None, 55)
    
    def textscreen(text,color,x,y):
        screentext = font.render(text, True, color)
        screen.blit(screentext, [x,y])
    
    while game:
        
        if score1>score2:
            text = "Player1 wins"
        elif score1<score2:
            text = "Player2 Wins"
        else:
            text = "The Game was Draw"
    
        def game_over():
            screen.fill("black")
            game_over_text = font.render(text, True, "Red")
            screen.fill("Black")
            screen.blit(game_over_text, (width/2-(game_over_text.get_width()/2),100))
    
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game = False
        
        screen.blit(back,(0,0))
        screen.blit(ball,(ballx,bally))
        screen.blit(kepp,(keppx, keppy))
        screen.blit(kepp2, (kepp2x,kepp2y))
        
        keys = pygame.key.get_pressed()
        
        #Moving first player
        if keys[pygame.K_UP] == True:
            if keppy != 0:
                keppy -= 10
                if keppy == 0:
                    keppy = 0
        
        if keys[pygame.K_DOWN] == True:
            if keppy != 500:
                keppy += 10
                if keppy == 500:
                    keppy = 500
        
        #Moving second player
        if keys[pygame.K_w] == True:
            if kepp2y != 0:
                kepp2y -= 10
                if kepp2y == 0:
                    kepp2y = 0
        
        if keys[pygame.K_s] == True:
            if kepp2y != 500:
                kepp2y += 10
                if kepp2y == 500:
                    kepp2y = 500
        
        if bal == True:
            ballx += vilx
            if ballx == 860:
                game_over()
                game = False
        
        if baly == True:
            bally += vily
            if bally == 560:
                baly = False
        
        if ballx == 125:
            if bally in range(keppy, keppy+120):
                 bal = True
                 score1 += 1
        
        if ballx == 700:
            if bally in range(kepp2y, kepp2y+120):
                bal = False
                score2 += 1
        
        if bal == False:
            ballx -= vilx
            if ballx == 0:
                game_over()
                game = False
        
        if baly == False:
            bally -= vily
            if bally == 0:
                baly = True
    
        textscreen("Score: "+ str(score1*10), "red", 5, 5)
        textscreen("Score: "+ str(score2*10), "red", 740, 5)
        pygame.display.update()
        clock.tick(60)

def opt():
    game = True
    while game:
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game = False
        
        screen.blit(opti,(0,0))
        
        if back_button.draw(screen):
            Game()
        
        pygame.display.update()

def Game():
    game = True
    screen.blit(wall,(0,0))
    while game:
        
        if start_button.draw(screen):
            run()
        if option_button.draw(screen):
            opt()
        if exit_button.draw(screen):
            game = False
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game = False

        pygame.display.update()

    pygame.quit()

Game()
pygame.quit()