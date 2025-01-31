import pygame.draw_py
from OpenGL.GL import *

class Mesh3D:
  def __init__(self):
    self.vertices = [(-0.5,-0.5,0.5),
            (0.5,-0.5,0.5),
            (0.5,0.5,0.5),
            (-0.5,0.5,0.5)]
    self.triangles = [0, 1, 2, 0, 2, 3]
    self.draw_type = GL_LINE_LOOP
    self.texture = pygame.image.load()
    self.texID = 0

  def init_texture(self):
      self.texID = glGenTextures(1)
      texture_data = pygame.image.tostring(self.texture, "RGB", True)
      width = self.texture.get_width()
      height = self.texture.get_height()
      glBindTexture(GL_TEXTURE_2D, self.texID)
      glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)
      glTexImage2D(GL_TEXTURE_2D, 0, 3, width, height, 0, GL_RGB, GL_UNSIGNED_BYTE, texture_data)

  def draw(self):
    for t in range(0, len(self.triangles), 3):
        glEnable(GL_TEXTURE_2D)
        glTexEnvf(GL_TEXTURE_ENV, GL_TEXTURE_ENV_MODE,GL_DECAL)
        glBindTexture(GL_TEXTURE_2D, self.texID)
        for t in range(0, len(self.triangles), 3):
            glBegin(self.draw_type)
            #print("tvalue: ", t);
            glTexCoord2fv(self.uvs[self.triangles[t]])
            glVertex3fv(self.vertices[self.triangles[t]])
            glTexCoord2fv(self.uvs[self.triangles[t + 1]])
            glVertex3fv(self.vertices[self.triangles[t + 1]])
            glTexCoord2fv(self.uvs[self.triangles[t + 2]])
            glVertex3fv(self.vertices[self.triangles[t + 2]])
            glEnd()
        glDisable(GL_TEXTURE_2D)