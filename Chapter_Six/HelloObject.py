import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
from Mesh3D import *
from Cube import *
from Object import *
from Transform import *

pygame.init()
screen_width = 768
screen_height = 768
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
#cube = Cube(GL_POLYGON, "../images/brick-wall.jpg")

objects = []

cube = Object("Cube")
cube.add_component(Transform((0, 0, -1)))
cube.add_component(Cube(GL_POLYGON, "../images/brick-wall.jpg"))

cube2 = Object("Cube2")
cube2.add_component(Transform((0, 1, 0)))
cube2.add_component(Cube(GL_POLYGON, "../images/brick-wall.jpg"))

objects.insert(0,cube)
objects.insert(1,cube2)

auto_rotate = False
clock = pygame.time.Clock()
fps = 30
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
        if event.key == pygame.K_SPACE:
            if auto_rotate:
                auto_rotate = False
            else:
                auto_rotate = True
        glRotatef(rotation_angle, rotation_x, rotation_y, 0)
    if event.type == pygame.QUIT:
      done = True
  glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
  if auto_rotate:
    glRotatef(1.25, 1, 0, 1)

  #mesh.draw()
  for o in objects:
      o.update()

  pygame.display.flip()
  clock.tick(fps)
  #pygame.time.wait(25);
  print('tick = {}, fps = {}'.format(clock.tick(), clock.get_fps()))
pygame.quit()