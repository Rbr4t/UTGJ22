# mängija, meteoriitide jms jaoks, hoiame asju natuke hajutatult siis on parem ülevaaade kui nad kõik ühes kohas on
import pygame
import random
from pygame.locals import *
class Player:
    def __init__(self,window, image):
        #self.image = pygame.image.load("pixil-frame-0.png")
        self.x = 320
        self.y = 540
        self.window = window
        self.image = image
        self.vel = 5
        self.isJump = False
        self.jumpCount = 5
        

    def draw(self):

        self.window.blit(self.image, (self.x, self.y))
        #pygame.display.flip()
    def sides(self, x, y):
        if self.x > self.window.get_width()-self.image.get_width():
            self.x = self.window.get_width()- self.image.get_width()
        elif self.x < 0:
            self.x = 0

class Meteor:
    def __init__(self):
        self.x = random.randint(0, 600)
        self.y = 0
        self.vx = 0
        self.vy = random.uniform(1, 2)
        self.img = pygame.image.load("test_subject.png")
    def update(self, dt):
        self.x += self.vx * dt
        self.y += self.vy * dt
        if(self.y > 480):
            self.die()
    def die(self):
        self.y = 0
        self.x = random.uniform(0, 640)
        self.vy = random.uniform(1, 2)
    def draw(self, s):
        s.blit(self.img, [self.x - self.img.get_width() / 2, self.y - self.img.get_height() / 2])