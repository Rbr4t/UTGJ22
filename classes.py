# mängija, meteoriitide jms jaoks, hoiame asju natuke hajutatult siis on parem ülevaaade kui nad kõik ühes kohas on
import pygame
import random
from pygame.locals import *

class Player:
    def __init__(self,window, image):
        #self.image = pygame.image.load("pixil-frame-0.png")
        self.x = 320
        self.y = 490
        self.window = window
        self.image = image
        self.vel = 5
        self.isJump = False
        self.jumpCount = 5

        self.hitbox = (self.x, self.y, 50, 50) # this
    def pplyr(self):
        return pygame.draw.rect(self.window, (255,0,0), self.hitbox,2)
    def draw(self):
        pygame.draw.rect(self.window, (255,0,0), self.hitbox,2)
        
        self.window.blit(self.image, (self.x, self.y)) # this
    def change(self):
        self.hitbox = (self.x, self.y+13, 100, 85) #hitbox
        
    def sides(self, x, y):
        if self.x > self.window.get_width()-self.image.get_width():
            self.x = self.window.get_width()- self.image.get_width()
        elif self.x < 0:
            self.x = 0

class Meteor:
    def __init__(self, window):
        self.window = window
        self.x = random.randint(0, window.get_size()[0])
        self.y = 0
        self.vx = 0
        self.vy = random.uniform(1, 2)
        self.meteoriidid = ("Kunst/Esemed/meteoriit1.png", "Kunst/Esemed/meteoriit2.png", "Kunst/Esemed/meteoriit3.png", "Kunst/Esemed/meteoriit4.png")
        self.img = pygame.image.load(self.meteoriidid[random.randint(0, 3)])
        self.hitbox = (self.x, self.y, 50, 50)
    def update(self, dt):
        self.x += self.vx * dt
        self.y += self.vy * dt
        if(self.y > (self.window.get_size()[1] - 40)):
            self.die()
    def ennmy(self):
        return pygame.draw.rect(self.window, (255,0,0), self.hitbox,2)
    def die(self):
        self.y = 0
        self.x = random.uniform(0, 800)
        self.vy = random.uniform(1, 2)
    def draw(self, s):
        s.blit(self.img, [self.x - self.img.get_width() / 2, self.y - self.img.get_height() / 2])
        self.hitbox = (self.x-15, self.y-15, 30, 30)

class Projectile:

    def __init__(self, x, y):
        self.x = x
        
        self.y = y
        self.radius = 10
        self.color = (0, 0, 0)
        self.vel = 10
        self.hitbox = (self.x, self.y, 10, 10)

    def draw(self, win):
        pygame.draw.circle(win, self.color, (self.x+25, self.y), self.radius)
        self.hitbox = (self.x+15, self.y-10, 20, 20) #hitbox'i väärtused
        #pygame.draw.rect(win, (255,0,0), self.hitbox,2)
    
    def bllt(self, win):
        return pygame.draw.rect(win, (255,0,0), self.hitbox,2)

    def die(self):
        self.y = -30