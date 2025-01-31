import pygame

from pygame.locals import *
def in_button(mpos, button):
    hit = False
    if mpos[0] > button[0] and mpos[0] < (button[0] + button[2]) and mpos[1] > button[1] and mpos[1] < (button[1] + button[3]):
        hit = True
    return hit


pygame.init()
screen_width = 800
screen_height = 800
screen = pygame.display.set_mode((screen_width, screen_height))
done = False
white = pygame.Color(255, 255, 255)
green = pygame.Color(0, 255, 0)
br_green = pygame.Color(100, 255, 100)
button_color = green
button = (0, 0, 100, 30)
mouse_down = False
last_mouse_pos = (0,0)
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == MOUSEBUTTONDOWN and event.button == 1:
            mouse_down = True
            last_mouse_pos = pygame.mouse.get_pos()
        elif event.type == MOUSEBUTTONUP and event.button == 1:
            mouse_down = False
        elif event.type == MOUSEMOTION and mouse_down is True:
            pygame.draw.line(screen, white, last_mouse_pos, pygame.mouse.get_pos(), 5)
            last_mouse_pos = pygame.mouse.get_pos()
            #pygame.draw.rect(screen, white,(pygame.mouse.get_pos(),(5, 5)))
        elif event.type == MOUSEBUTTONDOWN:
            if event.button == 1:
                pygame.draw.rect(screen, white, (pygame.mouse.get_pos(), (5, 5)))
        mpos = pygame.mouse.get_pos()
        if in_button(mpos, button):
            button_color = br_green
        else:
            button_color = green

    pygame.draw.rect(screen, button_color, button)
    pygame.display.update()
pygame.quit()