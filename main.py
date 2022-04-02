import pygame_menu
import classes
import pygame
import random
import classes

from pygame.locals import *

from menu import game_options, set_difficulty
global sounds


def main_menu():
    menu = pygame_menu.Menu('Muruniiduk', width, height,
                            theme=pygame_menu.themes.THEME_BLUE)

    menu.add.button('Mängi', start_the_game)
    menu.add.selector(
        'Rasusaste :', [('Raske', 1), ('Ei ole raske', 2)], onchange=set_difficulty)
    menu.add.button('Seaded', game_options(sounds))
    menu.add.button('Välju', pygame_menu.events.EXIT)
    return menu


def start_the_game():
    #bg = pygame.image.load("")
    saurusG_kõnnib = [pygame.image.load(
        "Kunst/Dinos/Green/dino_walk_r.png"), pygame.image.load("Kunst/Dinos/Green/dino_stand.png")]
    sarurusG_seisab = pygame.image.load("Kunst/Dinos/Pink/dino_stand_l.png")
    pygame.mixer.music.load('Kunst/Muusika/bgm.wav')
    pygame.mixer.music.play(-1)
    # char = sarurusG_seisab #suvaline pilt hetkel ei hakka praegu pilte lisama
    #window = pygame.display.set_mode([800, 600])
    korrad = 0
    RUN = True

    bullets = []
    # class to var
    player = classes.Player(window, sarurusG_seisab)
    bullet = classes.Projectile(player.x, player.y)
    # gamemodes
    easy = random.randint(1, 12)
    crazy = random.randint(12, 30)
    enemies = [classes.Meteor(window)
               for _ in range(crazy)]  # creating falling meteors

    shootLoop = 0
    clock = pygame.time.Clock()
    allowed_to_break = False
    paused = False
    while RUN:
        clock.tick(30)

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

        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            player.x -= player.vel
            if clock.get_time() % 3:
                player.image = pygame.image.load(
                    "Kunst/Dinos/Pink/dino_walk_l.png")
            elif clock.get_time() % 3 == 1:
                player.image = pygame.image.load(
                    "Kunst/Dinos/Pink/dino_walk_l_ii.png")
            else: 
                player.image = pygame.image.load(
                    "Kunst/Dinos/Pink/dino_stand_l.png")
        if keys[pygame.K_d]:
            player.x += player.vel
            if clock.get_time() % 2:
                player.image = pygame.image.load(
                    "Kunst/Dinos/Pink/dino_walk_r.png")
            else:
                player.image = pygame.image.load(
                    "Kunst/Dinos/Pink/dino_walk_r_ii.png")
        if keys[pygame.K_SPACE] and shootLoop == 0:
            if len(bullets) < 10:
                pygame.mixer.Sound.play(sounds[2])
                bullets.append(classes.Projectile(
                    round(player.x), round(player.y)))
            shootLoop = 1
        if keys[pygame.K_LCTRL]:
            paused = not paused
            if (paused):
                clock.tick(0)
            else:
                clock.tick(30)

        # jumping mechanism
        if not(player.isJump):

            if keys[pygame.K_w]:
                player.isJump = True
                player.image = pygame.image.load(
                    "Kunst/Dinos/Pink/dino_jump_l.png")
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

        player.draw()
        player.change()

        # meteoor
        dt = clock.get_time() / (1.0 / 60.0 * 1000)
        for enemy in enemies:
            for bullet in bullets:
                bullet.draw(window)
                if pygame.Rect.colliderect(bullet.bllt(window), enemy.ennmy()):
                    bullet.die()
                    enemy.die()
                    pygame.mixer.Sound.play(sounds[3])

        if enemies == []:
            enemies = [classes.Meteor(window) for _ in range(crazy)]
        for enemy in enemies:
            enemy.update(dt)
            enemy.draw(window)
            if pygame.Rect.colliderect(player.pplyr(), enemy.ennmy()):
                RUN = False
                pygame.mixer.Sound.play(sounds[1])
                enemies.remove(enemy)

        player.sides(player.x, player.y)

        image = pygame.image.load('setting_ico_smol.png').convert_alpha()
        pygame.display.update()


width = 800
height = 600
pygame.init()
pygame.mixer.init()
sounds = [pygame.mixer.Sound("Kunst/Muusika/jump.wav"), pygame.mixer.Sound("Kunst/Muusika/boom.wav"),
          pygame.mixer.Sound("Kunst/Muusika/shot2.wav"), pygame.mixer.Sound("Kunst/Muusika/meteorDown.wav")]
# pygame.mixer.Sound.set_volume(0.5)
window = pygame.display.set_mode([width, height])  # hetkel jätan nii suureks
main_menu().mainloop(window)
