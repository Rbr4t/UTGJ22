import pygame_menu
import classes
import pygame, random, classes

from pygame.locals import *

from button import button
from menu import game_options, set_difficulty

def main_menu():
    menu = pygame_menu.Menu('Muruniiduk', width, height,
                        theme=pygame_menu.themes.THEME_BLUE)

    menu.add.button('Mängi', start_the_game)
    menu.add.selector('Rasusaste :', [('Raske', 1), ('Ei ole raske', 2)], onchange=set_difficulty)
    menu.add.button('Seaded', game_options())
    menu.add.button('Välju', pygame_menu.events.EXIT)
    return menu


def start_the_game():
    char = pygame.image.load("pixil-frame-0.png") #srandom picture, I will later add right one
    #window = pygame.display.set_mode([800, 600])
    korrad = 0
    RUN = True
    
    bullets =[]
    player = classes.Player(window, char)
    bullet = classes.Projectile(player.x, player.y)
    easy = random.randint(1, 12)
    crazy = random.randint(12, 30)
    enemies = [classes.Meteor(window) for _ in range(crazy)]
    shootLoop = 0
    clock = pygame.time.Clock()
    allowed_to_break = False
    while RUN:
        clock.tick(30)
        
        if shootLoop > 0:
            shootLoop += 1
        if shootLoop > 3:
            shootLoop = 0

        for bullet in bullets:
            if bullet.y < 800 and bullet.y > 0:
                bullet.y -= bullet.vel
            else:
                bullets.pop(bullets.index(bullet))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                RUN = False

        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:  
            player.x -= player.vel

        if keys[pygame.K_d]: 
            player.x += player.vel
        if keys[pygame.K_SPACE] and shootLoop == 0:
            if len(bullets) < 10:
                bullets.append(classes.Projectile(round(player.x), round(player.y)))
            shootLoop = 1
        
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
                player.y = 490
        
        
        
        window.fill((255,255,255))
        
        player.draw()
        player.change()
        
        if enemies == []:
            enemies = [classes.Meteor(window) for _ in range(crazy)]
        
        #meteoor
        dt = clock.get_time() / (1.0 / 60.0 * 1000)
        for bullet in bullets:
            bullet.draw(window)
        for enemy in enemies:
            enemy.update(dt)
            enemy.draw(window)
            if pygame.Rect.colliderect(player.pplyr(), enemy.ennmy()):
                print("Hello!")
                enemies.remove(enemy)
            
        player.sides(player.x, player.y)
        #ground.draw()
        image = pygame.image.load('setting_ico_smol.png').convert_alpha()
        pygame.display.update()
width = 800
height = 600
pygame.init()
window = pygame.display.set_mode([width, height]) # hetkel jätan nii suureks
main_menu().mainloop(window)
