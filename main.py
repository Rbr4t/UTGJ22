import pygame
import classes
from pygame.locals import *

pygame.init()
window = pygame.display.set_mode([800, 600]) # hetkel jätan nii suureks
char = pygame.image.load("pixil-frame-0.png") #suvaline pilt hetkel ei hakka praegu pilte lisama
RUN = True
x = 320
y = 140
player = classes.Player(window, x, y, char)
clock = pygame.time.Clock()
while RUN: #gameloop
    
    #print([player.x, y])
    dt = clock.tick(30)
    keys=pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            RUN = False
        
        if keys[K_a]:
            player.x -= player.vel

        if keys[K_d]:
            player.x += player.vel
         

    window.fill([255, 255, 255])
    player.draw(dt)
    pygame.display.flip()
    
    
pygame.quit()
