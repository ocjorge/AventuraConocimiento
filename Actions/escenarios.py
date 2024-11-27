#escenarios.py
import pygame
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from pygame.locals import *
from PIL import Image

pygame.init()
pygame.mixer.init()

def load_texture(filename):
    im = Image.open(filename)
    ix, iy = im.size
    image = im.tobytes("raw", "RGBA", 0, -1)  # Usa RGBA si quieres transparencia
    texture_id = glGenTextures(1)
    glBindTexture(GL_TEXTURE_2D, texture_id)
    glPixelStorei(GL_UNPACK_ALIGNMENT,1)
    

    # Cargar la textura
    glTexImage2D(GL_TEXTURE_2D, 0, GL_RGBA, ix, iy, 0, GL_RGBA, GL_UNSIGNED_BYTE, image)
    
    # Establecer parámetros de textura
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_REPEAT)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_REPEAT)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)

    return texture_id

def draw_escenario(fileImage):
     #Habilita el uso de texturas 2D en OpenGL
    glEnable(GL_TEXTURE_2D)
    #Vincula la textura la imagen que mandamos
    glBindTexture(GL_TEXTURE_2D, load_texture(fileImage))
    
    #Inicia el dibujo-
    #GL_QUADS(indica que sera compuesto por cuadrilateros)
    glBegin(GL_QUADS)
    
    # Cara frontal
    glColor3f(1, 1, 1)
    glTexCoord2f(0, 0)
    glVertex3f(-50, -50, 50)
    glTexCoord2f(1, 0)
    glVertex3f(50, -50, 50)
    glTexCoord2f(1, 1)
    glVertex3f(50, 50, 50)
    glTexCoord2f(0, 1)
    glVertex3f(-50, 50, 50)
    
    # Cara trasera
    glTexCoord2f(0, 0)
    glVertex3f(-50, -50, -50)
    glTexCoord2f(1, 0)
    glVertex3f(50, -50, -50)
    glTexCoord2f(1, 1)
    glVertex3f(50, 50, -50)
    glTexCoord2f(0, 1)
    glVertex3f(-50, 50, -50)
    
    # Cara izquierda
    glTexCoord2f(0, 0)
    glVertex3f(-50, -50, -50)
    glTexCoord2f(1, 0)
    glVertex3f(-50, -50, 50)
    glTexCoord2f(1, 1)
    glVertex3f(-50, 50, 50)
    glTexCoord2f(0, 1)
    glVertex3f(-50, 50, -50)
    
    # Cara derecha
    glTexCoord2f(0, 0)
    glVertex3f(50, -50, -50)
    glTexCoord2f(1, 0)
    glVertex3f(50, -50, 50)
    glTexCoord2f(1, 1)
    glVertex3f(50, 50, 50)
    glTexCoord2f(0, 1)
    glVertex3f(50, 50, -50)
    
    # Cara superior
    glTexCoord2f(0, 0)
    glVertex3f(-50, 50, -50)
    glTexCoord2f(1, 0)
    glVertex3f(50, 50, -50)
    glTexCoord2f(1, 1)
    glVertex3f(50, 50, 50)
    glTexCoord2f(0, 1)
    glVertex3f(-50, 50, 50)
    
    # Cara inferior
    glTexCoord2f(0, 0)
    glVertex3f(-50, -50, -50)
    glTexCoord2f(1, 0)
    glVertex3f(50, -50, -50)
    glTexCoord2f(1, 1)
    glVertex3f(50, -50, 50)
    glTexCoord2f(0, 1)
    glVertex3f(-50, -50, 50)


    glEnd()
    glDisable(GL_TEXTURE_2D)
