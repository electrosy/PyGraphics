import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
from Mesh3D import *

class Cube(Mesh3D):
  def __init__(self, draw_type, filename):
      A = (-0.5, -0.5, -0.5)
      B = (0.5, -0.5, -0.5)
      C = (0.5, 0.5, -0.5)
      D = (-0.5, 0.5, -0.5)
      E = (-0.5, -0.5, 0.5)
      F = (0.5, -0.5, 0.5)
      G = (0.5, 0.5, 0.5)
      H = (-0.5, 0.5, 0.5)

      self.vertices = [F, E, G, H,
                       C, D, B, A,
                       G, H, C, D,
                       B, F, E, A,
                       E, H, D, A,
                       B, C, G, F
                       ]

      self.triangles = [0, 2, 3, 0, 3, 1,
                        8, 4, 5, 8, 5, 9,
                        10, 6, 7, 10, 7, 11,
                        12, 13, 14, 12, 14, 15,
                        16, 17, 18, 16, 18, 19,
                        20, 21, 22, 20, 22, 23]

      self.uvs = [(0.0, 0.0),
                  (1.0, 0.0),
                  (0.0, 1.0),
                  (1.0, 1.0),
                  (0.0, 1.0),
                  (1.0, 1.0),
                  (0.0, 1.0),
                  (1.0, 1.0),
                  (0.0, 0.0),
                  (1.0, 0.0),
                  (0.0, 0.0),
                  (1.0, 0.0),
                  (0.0, 0.0),
                  (0.0, 1.0),
                  (1.0, 1.0),
                  (1.0, 0.0),
                  (0.0, 0.0),
                  (0.0, 1.0),
                  (1.0, 1.0),
                  (1.0, 0.0),
                  (0.0, 0.0),
                  (0.0, 1.0),
                  (1.0, 1.0),
                  (1.0, 0.0)]
      Mesh3D.texture = pygame.image.load(filename)
      Mesh3D.draw_type = draw_type
      Mesh3D.init_texture(self)


pygame.init()
screen_width = 500
screen_height = 500
screen = pygame.display.set_mode((screen_width, screen_height), DOUBLEBUF|OPENGL)
pygame.display.set_caption('OpenGL in Python')
done = False
white = pygame.Color(255, 255, 255)
glMatrixMode(GL_PROJECTION)
#gluPerspective(60, (screen_width / screen_height), 0.1, 100.0)
glOrtho(-1, 1, 1, -1, 0.1, 100.0)
glMatrixMode(GL_MODELVIEW)
translate = -2
translate_to = 0
rotation_x = 0
rotation_y = 0
rotation_angle = 0
rotation_angle_step = 11.25
glTranslatef(0.0, 0.0, translate)
glEnable(GL_DEPTH_TEST)
glEnable(GL_LIGHTING)

glLight(GL_LIGHT0, GL_POSITION, (5, 5, 5, 1))
#glLightfv(GL_LIGHT0, GL_AMBIENT, (0, 1, 0, 1))
glLightfv(GL_LIGHT0, GL_DIFFUSE, (1, 1, 1, 1))
#glLightfv(GL_LIGHT0, GL_SPECULAR, (0, 1, 0, 1))

#glLight(GL_LIGHT1, GL_POSITION, (-5, 5, 0, 1))
#glLightfv(GL_LIGHT1, GL_DIFFUSE, (0, 0, 1, 1))

glEnable(GL_LIGHT0)
#glEnable(GL_LIGHT1)

glMaterialfv(GL_FRONT, GL_DIFFUSE, (0, 1, 0, 1))

#mesh = Mesh3D()
cube = Cube(GL_POLYGON, "brick-wall.jpg")

while not done:
  for event in pygame.event.get():
    if event.type == pygame.MOUSEWHEEL:
        print(event.x, event.y)
        translate_to = 0
        if event.y == 1:
            translate_to += 0.1
        elif event.y == -1:
            translate_to -= 0.1
        print("translate: ", translate_to)
        glTranslatef(0.0, 0.0, translate_to)
    if event.type == pygame.KEYDOWN:
        rotation_y = 0
        rotation_x = 0
        rotation_angle = 0
        if event.key == pygame.K_LEFT:
            rotation_y = 1
            rotation_angle = -rotation_angle_step
        if event.key == pygame.K_RIGHT:
            rotation = rotation_y = 1
            rotation_angle = rotation_angle_step
        if event.key == pygame.K_UP:
            rotation_x = 1
            rotation_angle = -rotation_angle_step
        if event.key == pygame.K_DOWN:
            rotation = rotation_x = 1
            rotation_angle = rotation_angle_step
        glRotatef(rotation_angle, rotation_x, rotation_y, 0)
    if event.type == pygame.QUIT:
      done = True
  glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
  #glRotatef(5, 1, 0, 1)

  #mesh.draw()
  cube.draw()
  pygame.display.flip()
  pygame.time.wait(100);
pygame.quit()