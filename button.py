import pygame

def button(x, y, w, h, ic, ac, img, imgon, action, window):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    rect = pygame.Rect(x, y, w, h)
    on_button = rect.collidepoint(mouse)
    if on_button:
        pygame.draw.rect(window, ac, rect)
        window.blit(imgon, imgon.get_rect(center = rect.center))
    else:
        pygame.draw.rect(window, ic, rect)
        window.blit(img, img.get_rect(center = rect.center))

    if on_button:  
        if click[0] == 1 and action!= None:
            action()