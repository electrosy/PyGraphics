import math
import pygame

pygame.init()

screen_width = 400
screen_height = 400
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Naive Circle')
done = False
white = pygame.Color(255, 255, 255)
radius = 50
center = (200, 200)

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    for x in range(-50, 50):
        y = math.sqrt(math.pow(radius, 2) - math.pow(x, 2))
        screen.set_at((int(x + center[0]), int(y + center[1])), white)
        y = -math.sqrt(math.pow(radius, 2) - math.pow(x, 2))
        screen.set_at((int(x + center[0]), int(y + center[1])), white)
    pygame.display.update()
pygame.quit()