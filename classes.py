# mängija, meteoriitide jms jaoks, hoiame asju natuke hajutatult siis on parem ülevaaade kui nad kõik ühes kohas on
import pygame

from pygame.locals import *
class Player:
    def __init__(self,window, x, y, image, vel=10):
        #self.image = pygame.image.load("pixil-frame-0.png")
        self.x = x
        self.y = y
        self.window = window
        self.image = image
        self.vel = vel
        

    def draw(self, dt):

        self.window.blit(self.image, (self.x, self.y))
        #pygame.display.flip()