import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
from Mesh3D import *

class Cube(Mesh3D):
  def __init__(self):
    self.vertices = [(-0.5,-0.5,0.5),
            (0.5,-0.5,0.5),
            (0.5,0.5,0.5),
            (-0.5,0.5,0.5),
            (-0.5, -0.5, -0.5),
            (0.5,-0.5,-0.5),
            (0.5, 0.5, -0.5),
            (-0.5,0.5,-0.5)]
    self.triangles = [0, 1, 2, 0, 2, 3, 4, 5, 6, 4, 6, 7, 4, 5, 1, 4, 1, 0, 5, 6, 2, 5, 2, 1, 6, 7, 3, 6, 3, 2, 7, 4, 0, 7, 0, 3, 4, 5, 1, 4, 1, 0]

pygame.init()
screen_width = 500
screen_height = 500
screen = pygame.display.set_mode((screen_width, screen_height), DOUBLEBUF|OPENGL)
pygame.display.set_caption('OpenGL in Python')
done = False
white = pygame.Color(255, 255, 255)
gluPerspective(60, (screen_width / screen_height), 0.1, 100.0)
#glOrtho(-1, 1, 1, -1, 0.1, 100.0)
glTranslatef(0.0, 0.0, -3)


mesh = Mesh3D()
cube = Cube()

while not done:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      done = True
  glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
  glRotatef(5, 1, 0, 1)
  #mesh.draw()
  cube.draw()
  pygame.display.flip()
  pygame.time.wait(100);
pygame.quit()