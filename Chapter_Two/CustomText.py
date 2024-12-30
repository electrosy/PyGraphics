import pygame

pygame.init()

screen_width = 800

screen_height = 200

screen = pygame.display.set_mode((screen_width, screen_height))

done = False

white = pygame.Color(255, 255, 255)

pygame.font.init()

font = pygame.font.Font('Super Theory.ttf', 120)

text = font.render('Steven Philley', False, white)

while not done:

  for event in pygame.event.get():

    if event.type == pygame.QUIT:

      done = True

  screen.blit(text, (10, 10))

  pygame.display.update()

pygame.quit()