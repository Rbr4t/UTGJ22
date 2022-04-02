import pygame
from pygame.locals import *

pygame.init()
window = pygame.display.set_mode([800, 600]) # hetkel jätan nii suureks
char = pygame.image.load("pixil-frame-0.png")
RUN = True

clock = pygame.time.Clock()
while RUN: #gameloop
    dt = clock.tick() / 1000
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            RUN = False

pygame.quit()