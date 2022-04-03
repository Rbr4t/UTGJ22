import pygame_menu
import classes
import pygame
import random
import classes
import time

from pygame.locals import *
from menu import game_options

global sounds
global DinoPath
global meteorite_amount
global round_ammo
round_ammo = 3
meteorite_amount = random.randint(60, 85)


def set_difficulty(difficulty):
    global round_ammo
    global meteorite_amount
    #print(round_ammo)
    if difficulty == 1: #Hard
        round_ammo = 3 #ammo
        meteorite_amount = random.randint(60, 85) #meteorites
    else: #not so hard
        print("kerge")
        round_ammo = 7 #ammo
        meteorite_amount = random.randint(10, 19) #meteorites

def main_menu():
    menu = pygame_menu.Menu('Muruniiduk', width, height,
                            theme=pygame_menu.themes.THEME_BLUE)

    menu.add.button('PLAY', start_the_game)
    menu.add.selector(
        'Difficulity :', [('Hard', 1), ('Normal', 2)], onchange=lambda x, index : set_difficulty(index))
    menu.add.button('Settings', game_options(sounds,DinoPath))
    menu.add.button('Exit', pygame_menu.events.EXIT)
    return menu


def start_the_game():
    saurus = {'walkL': [pygame.image.load(DinoPath[0]+"dino_walk_l.png"), pygame.image.load(DinoPath[0]+"dino_walk_l_ii.png")],
              'walkR': [pygame.image.load(DinoPath[0]+"dino_walk_r.png"), pygame.image.load(DinoPath[0]+"dino_walk_r_ii.png")],
              'jumpL': [pygame.image.load(DinoPath[0]+"dino_jump_l.png")],
              'jumpR': [pygame.image.load(DinoPath[0]+"dino_jump_r.png")],
              'standL': [pygame.image.load(DinoPath[0]+"dino_stand_l.png")],
              'standR': [pygame.image.load(DinoPath[0]+"dino_stand_r.png")],
              }
    #bg = pygame.image.load("")
    sarurusG_seisab = pygame.image.load("Kunst/Dinos/Pink/dino_stand_l.png")
    pygame.mixer.music.load('Kunst/Muusika/bgm.wav')
    heart = pygame.image.load("Kunst/Esemed/heart.png")
    pygame.mixer.music.play(-1)
    taust = pygame.image.load("Kunst/Esemed/taust.png")
    # char = sarurusG_seisab #suvaline pilt hetkel ei hakka praegu pilte lisama
    #window = pygame.display.set_mode([800, 600])
    korrad = 0
    RUN = True

    


    muru = pygame.image.load("Kunst/Esemed/muru.png")

    bullets = []
    # class to var
    player = classes.Player(window, saurus["standL"][0])
    bullet = classes.Projectile(player.x, player.y)
    # gamemodes
    global round_ammo
    global meteorite_amount #= random.randint(50, 130) # crazy == gamemod. chan
    
    meteorite_amount
    enemies = [classes.Meteor(window)
               for _ in range(meteorite_amount)]  # creating falling meteors
    
    #HUD elemdid
    hearts = 3
    listed_hearts = [(heart, (0, 0)), (heart, (40, 0)), (heart, (80, 0))]

    myfont = pygame.font.SysFont("Arial", 25)
    score = 0
    double_points = False

    #Aeg
    counter = 10
    pygame.time.set_timer(pygame.USEREVENT, 1000)
    font = pygame.font.SysFont('Consolas', 30)
    
    shootLoop = 0
    clock = pygame.time.Clock()
    crazy_mode = False
    
    M = 1
    while RUN and hearts > 0:
        #time remaining         
        if counter == 0:
            if M%2 != 0:
                new_meteorites = [classes.Meteor(window)
                for _ in range(int(meteorite_amount/2))]
                enemies.extend(new_meteorites)
                double_points = True
                counter = 20
            else:
                counter = 120
                new_meteorites = [classes.Meteor(window)
                for _ in range(meteorite_amount+12)]
                enemies.extend(new_meteorites)
                double_points = False
                counter = 10
            M += 1
            
        



        clock.tick(30)
        countersurface = myfont.render(f"Timer: {counter}", False, (0, 0, 0))
        textsurface = myfont.render(f"Score: {score}", False, (0, 0, 0))
        # bullets
        if shootLoop > 0:
            shootLoop += 1
        if shootLoop > 3:
            shootLoop = 0

        for bullet in bullets:
            if bullet.y < 800 and bullet.y > 0:
                bullet.y -= bullet.vel
            else:
                bullets.pop(bullets.index(bullet))

        # user input
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                RUN = False
            if event.type == pygame.USEREVENT: 
                counter -= 1
                
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            player.x -= player.vel
            if DinoPath[0] == player.image != "Kunst/Dinos/Green/":
                if clock.get_time() % 3:
                    player.image = saurus["walkL"][0]
                elif clock.get_time() % 3 == 1:
                    player.image = saurus["walkL"][1]
                else:
                    player.image = saurus["standL"][0]
            else:
                if clock.get_time() % 2:
                    player.image = saurus["walkL"][0]
                else:
                    player.image = saurus["standL"][0]
        if keys[pygame.K_d]:
            player.x += player.vel
            if DinoPath[0] == player.image != "Kunst/Dinos/Green/":
                if clock.get_time() % 2:
                    player.image = saurus["walkR"][0]
                else:
                    player.image = saurus["walkR"][1]
            else:
                if clock.get_time() % 2:
                    player.image = saurus["walkR"][0]
                else:
                    player.image = saurus["standR"][0]
        if keys[pygame.K_SPACE] and shootLoop == 0:
            if len(bullets) < round_ammo: #round ammo
                pygame.mixer.Sound.play(sounds[2])
                bullets.append(classes.Projectile(
                    round(player.x), round(player.y)))
            shootLoop = 1

        # jumping mechanism
        if not(player.isJump):

            if keys[pygame.K_w]:
                player.isJump = True
                player.image = saurus["jumpL"][0]
                pygame.mixer.Sound.play(sounds[0])
        else:
            if player.jumpCount >= -8:
                player.y -= (player.jumpCount * abs(player.jumpCount)) * 0.5
                player.jumpCount -= 1
            else:
                player.jumpCount = 10
                player.isJump = False
                player.y = 490

        window.fill((255, 255, 255))
        window.blit(taust, (0, 0))
        player.draw()
        player.change()

        window.blit(muru, (0, -5))

        #HUD elemendid

        window.blit(textsurface, (width-120, 0))
        window.blit(countersurface, (340, 0))
        for heart in listed_hearts:
            window.blit(heart[0], heart[1])


        # meteoor
        dt = clock.get_time() / (1.0 / 60.0 * 1000)
        for enemy in enemies:
            for bullet in bullets:
                bullet.draw(window)
                if pygame.Rect.colliderect(bullet.bllt(window), enemy.ennmy()):
                    bullet.die()
                    score += 1
                    if double_points:
                         score += 1
                    enemy.die()
                    pygame.mixer.Sound.play(sounds[3])

        if enemies == []:
            enemies = [classes.Meteor(window) for _ in range(meteorite_amount)]
        for enemy in enemies:
            enemy.update(dt)
            enemy.draw(window)
            if pygame.Rect.colliderect(player.pplyr(), enemy.ennmy()):
                hearts -= 1
                
                listed_hearts.pop(-1)
                pygame.mixer.Sound.play(sounds[1])
                enemies.remove(enemy)

        player.sides(player.x, player.y)
        
        image = pygame.image.load('setting_ico_smol.png').convert_alpha()
        pygame.display.update()
    

global width, height
width = 800
height = 600
pygame.init()
pygame.mixer.init()
pygame.font.init()
sounds = [pygame.mixer.Sound("Kunst/Muusika/jump.wav"), pygame.mixer.Sound("Kunst/Muusika/boom.wav"),
          pygame.mixer.Sound("Kunst/Muusika/shot2.wav"), pygame.mixer.Sound("Kunst/Muusika/meteorDown.wav")]
DinoPath = ["Kunst/Dinos/Green/"]
pygame.display.set_caption("DinoDeath")  # name
# pygame.mixer.Sound.set_volume(0.5)
window = pygame.display.set_mode([width, height])  # hetkel jätan nii suureks
main_menu().mainloop(window)
