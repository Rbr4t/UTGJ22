import pygame, random, classes
pygame.init()

win = pygame.display.set_mode((800,600))
char = pygame.image.load("pixil-frame-0.png") #suvaline pilt hetkel ei hakka praegu pilte lisama

korrad = 0
RUN = True
player = classes.Player(win, char)


clock = pygame.time.Clock()

while RUN:
    clock.tick(30)


    
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            RUN = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_a]:  
        player.x -= player.vel

    if keys[pygame.K_d]: 
        player.x += player.vel
    
    #jumping mechanism
    if not(player.isJump): 

        if keys[pygame.K_w]:
            player.isJump = True
    else:
        if player.jumpCount >= -8:
            player.y -= (player.jumpCount * abs(player.jumpCount)) * 0.5
            player.jumpCount -= 1
        else: 
            player.jumpCount = 10
            player.isJump = False
            player.y = 540
    
    
    
    win.fill((255,255,255))
    
    player.draw()
    
    
    player.sides(player.x, player.y)
    #ground.draw()
    pygame.display.update()
    
pygame.quit()