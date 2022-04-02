# mängija, meteoriitide jms jaoks, hoiame asju natuke hajutatult siis on parem ülevaaade kui nad kõik ühes kohas on
import pygame

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