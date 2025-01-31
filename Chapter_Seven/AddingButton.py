from Object import *
from Cube import *
import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
from Button import *

pygame.init()
screen_width = 800
screen_height = 600
pygame.display.set_caption('OpenGL in Python')
screen = pygame.display.set_mode((screen_width,screen_height),DOUBLEBUF | OPENGL)
done = False
objects_3d = []
objects_2d = []
cube = Object("Cube")

cube.add_component(Transform((0, 0, -5)))
cube.add_component(Cube(GL_POLYGON,"../images/brick-wall.jpg"))
objects_3d.append(cube)

white = pygame.Color(255, 255, 255)
green = pygame.Color(0, 255, 0)
blue = pygame.Color(0, 0, 255)
button1 = Object("Button")
button1.add_component(Button(screen, (0, 0), 100, 50,white, green, blue))
objects_2d.append(button1)
clock = pygame.time.Clock()
fps = 30

def set_2d():
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()  # reset projection matrix
    gluOrtho2D(0, 1600, 0, 1200)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()  # reset modelview matrix
    glViewport(0, 0, screen.get_width(),screen.get_height())
def set_3d():
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(60, (screen_width / screen_height),0.1, 100.0)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    glViewport(0, 0, screen.get_width(),screen.get_height())
    glEnable(GL_DEPTH_TEST)

while not done:
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            done = True
    glPushMatrix()
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    set_3d()
    for o in objects_3d:
        o.update(events)
    set_2d()
    for o in objects_2d:
        o.update(events)
    glPopMatrix()
    pygame.display.flip()
    clock.tick(fps)
pygame.quit()