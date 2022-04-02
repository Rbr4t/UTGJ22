import pygame_menu
import classes
import pygame, random, classes

from pygame.locals import *

from menu import game_options, set_difficulty

def main_menu():
    menu = pygame_menu.Menu('Muruniiduk', 600, 400,
                        theme=pygame_menu.themes.THEME_BLUE)

    menu.add.button('Mängi', start_the_game)
    menu.add.selector('Rasusaste :', [('Raske', 1), ('Ei ole raske', 2)], onchange=set_difficulty)
    menu.add.button('Seaded', game_options())
    menu.add.button('Välju', pygame_menu.events.EXIT)
    return menu


def start_the_game():
    char = pygame.image.load("pixil-frame-0.png") #suvaline pilt hetkel ei hakka praegu pilte lisama

    korrad = 0
    RUN = True
    player = classes.Player(window, char)


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
        
        
        
        window.fill((255,255,255))
        
        player.draw()
        
        
        player.sides(player.x, player.y)
        #ground.draw()
        pygame.display.update()

pygame.init()
window = pygame.display.set_mode([800, 600]) # hetkel jätan nii suureks
main_menu().mainloop(window)
