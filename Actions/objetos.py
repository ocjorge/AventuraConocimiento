#objetos.py
import pygame
import numpy 
import math
from pygame.locals import *
from PIL import Image
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

from Actions import colisiones

# Colores
BLUE = (0, 0, 1)
RED = (1, 0, 0)
GREEN = (0, 1, 0)
YELLOW = (1, 1, 0)
PURPLE = (1, 0, 1)
WHITE = (1, 1, 1)
BLACK = (0, 0, 0)
ORANGE = (1.0, 0.5, 0.0)

def create_cube(x, y, z, size):
    vertices = (
        (x-size, y-size, z-size),
        (x+size, y-size, z-size),
        (x+size, y+size, z-size),
        (x-size, y+size, z-size),
        (x-size, y-size, z+size),
        (x+size, y-size, z+size),
        (x+size, y+size, z+size),
        (x-size, y+size, z+size)
    )

    edges = (
        (0,1), (1,2), (2,3), (3,0),
        (4,5), (5,6), (6,7), (7,4),
        (0,4), (1,5), (2,6), (3,7)
    )

    glBegin(GL_LINES)
    for edge in edges:
        for vertex in edge:
            glVertex3fv(vertices[vertex])
    glEnd()

    

def create_sphere(radius, num_slices, num_stacks):
    for i in range(num_stacks):
        lat0 = math.pi * (-0.5 + float(i) / num_stacks)
        z0 = math.sin(lat0)
        zr0 = math.cos(lat0)

        lat1 = math.pi * (-0.5 + float(i + 1) / num_stacks)
        z1 = math.sin(lat1)
        zr1 = math.cos(lat1)

        glBegin(GL_QUAD_STRIP)
        for j in range(num_slices + 1):
            lng = 2 * math.pi * float(j) / num_slices
            x = math.cos(lng)
            y = math.sin(lng)

            glNormal3f(x * zr0, y * zr0, z0)
            glVertex3f(radius * x * zr0, radius * y * zr0, radius * z0)
            glNormal3f(x * zr1, y * zr1, z1)
            glVertex3f(radius * x * zr1, radius * y * zr1, radius * z1)
        glEnd()


def draw_cube():
    glColor3f(1.0, 0.0, 0.0)  
    glBegin(GL_QUADS)
    
    # Cara frontal
    glColor3f(0.8, 0.2, 0.2)
    glNormal3f(0.0, 0.0, 1.0)
    glVertex3f(-1.0, -1.0, 1.0)
    glVertex3f(1.0, -1.0, 1.0)
    glVertex3f(1.0, 1.0, 1.0)
    glVertex3f(-1.0, 1.0, 1.0)

    # Cara trasera
    glColor3f(0.8, 0.2, 0.2)
    glNormal3f(0.0, 0.0, 1.0)
    glVertex3f(-1.0, -1.0, -1.0)
    glVertex3f(1.0, -1.0, -1.0)
    glVertex3f(1.0, 1.0, -1.0)
    glVertex3f(-1.0, 1.0, -1.0)

    # Caras laterales
    glColor3f(0.8, 0.2, 0.2)
    glNormal3f(0.0, 0.0, 1.0)
    glVertex3f(-1.0, -1.0, 1.0)
    glVertex3f(1.0, -1.0, 1.0)
    glVertex3f(1.0, -1.0, -1.0)
    glVertex3f(-1.0, -1.0, -1.0)

    glColor3f(0.8, 0.2, 0.2)
    glNormal3f(0.0, 0.0, 1.0)
    glVertex3f(-1.0, 1.0, 1.0)
    glVertex3f(1.0, 1.0, 1.0)
    glVertex3f(1.0, 1.0, -1.0)
    glVertex3f(-1.0, 1.0, -1.0)

    glColor3f(0.8, 0.2, 0.2)
    glNormal3f(0.0, 0.0, 1.0)
    glVertex3f(-1.0, -1.0, 1.0)
    glVertex3f(-1.0, 1.0, 1.0)
    glVertex3f(-1.0, 1.0, -1.0)
    glVertex3f(-1.0, -1.0, -1.0)

    glColor3f(0.8, 0.2, 0.2)
    glVertex3f(1.0, -1.0, 1.0)
    glVertex3f(1.0, 1.0, 1.0)
    glVertex3f(1.0, 1.0, -1.0)
    glVertex3f(1.0, -1.0, -1.0)

    glEnd()

def draw_cube_dos():
    glColor3f(0.5, 0.0, 0.5)
    glBegin(GL_QUADS)

    # Cara frontal
    glColor3f(0.2, 0.2, 0.8)
    glNormal3f(0.0, 0.0, 1.0)
    glVertex3f(-2.0, -2.0, 2.0)
    glVertex3f(2.0, -2.0, 2.0)
    glVertex3f(2.0, 2.0, 2.0)
    glVertex3f(-2.0, 2.0, 2.0)

    # Cara trasera
    glColor3f(0.2, 0.2, 0.8)
    glNormal3f(0.0, 0.0, 1.0)
    glVertex3f(-2.0, -2.0, -2.0)
    glVertex3f(2.0, -2.0, -2.0)
    glVertex3f(2.0, 2.0, -2.0)
    glVertex3f(-2.0, 2.0, -2.0)

    # Caras laterales
    glColor3f(0.2, 0.2, 0.8)
    glNormal3f(0.0, 0.0, 1.0)
    glVertex3f(-2.0, -2.0, 2.0)
    glVertex3f(2.0, -2.0, 2.0)
    glVertex3f(2.0, -2.0, -2.0)
    glVertex3f(-2.0, -2.0, -2.0)

    glColor3f(0.2, 0.2, 0.8)
    glNormal3f(0.0, 0.0, 1.0)
    glVertex3f(-2.0, 2.0, 2.0)
    glVertex3f(2.0, 2.0, 2.0)
    glVertex3f(2.0, 2.0, -2.0)
    glVertex3f(-2.0, 2.0, -2.0)

    glColor3f(0.2, 0.2, 0.8)
    glNormal3f(0.0, 0.0, 1.0)
    glVertex3f(-2.0, -2.0, 2.0)
    glVertex3f(-2.0, 2.0, 2.0)
    glVertex3f(-2.0, 2.0, -2.0)
    glVertex3f(-2.0, -2.0, -2.0)

    glColor3f(0.2, 0.2, 0.8)
    glNormal3f(0.0, 0.0, 1.0)
    glVertex3f(2.0, -2.0, 2.0)
    glVertex3f(2.0, 2.0, 2.0)
    glVertex3f(2.0, 2.0, -2.0)
    glVertex3f(2.0, -2.0, -2.0)

    glEnd()

def draw_pyramid(pos_x, pos_y, pos_z, size):
    glPushMatrix()
    glTranslatef(pos_x, pos_y, pos_z)
    glBegin(GL_TRIANGLES)

    # Cara frontal
    glColor3f(1.0, 0.0, 0.0)
    glVertex3f(0.0, size, 0.0)
    glVertex3f(-size, -size, size)
    glVertex3f(size, -size, size)

    # Cara trasera
    glColor3f(0.0, 1.0, 0.0)
    glVertex3f(0.0, size, 0.0)
    glVertex3f(-size, -size, -size)
    glVertex3f(size, -size, -size)

    # Cara izquierda
    glColor3f(0.0, 0.0, 1.0)
    glVertex3f(0.0, size, 0.0)
    glVertex3f(-size, -size, size)
    glVertex3f(-size, -size, -size)

    # Cara derecha
    glColor3f(1.0, 1.0, 0.0)
    glVertex3f(0.0, size, 0.0)
    glVertex3f(size, -size, size)
    glVertex3f(size, -size, -size)

    # Cara base
    glColor3f(0.0, 1.0, 1.0)
    glVertex3f(-size, -size, size)
    glVertex3f(size, -size, size)
    glVertex3f(size, -size, -size)
    glVertex3f(-size, -size, -size)

    glEnd()
    glPopMatrix()

def draw_cylinder(pos_x, pos_y, pos_z, radius, height, slices=20):
    glPushMatrix()
    glTranslatef(pos_x, pos_y, pos_z)

    # Dibuja el cilindro
    glBegin(GL_QUAD_STRIP)
    for i in range(slices + 1):
        angle = 2.0 * math.pi * float(i) / float(slices)  # Usar math.pi
        x = radius * math.cos(angle)  # Usar math.cos
        z = radius * math.sin(angle)  # Usar math.sin

        glNormal3f(x, 0, z)
        glVertex3f(x, height / 2.0, z)
        glVertex3f(x, -height / 2.0, z)
    glEnd()

    # Dibuja las tapas del cilindro
    glBegin(GL_TRIANGLE_FAN)
    glNormal3f(0, 1, 0)
    glVertex3f(0, height / 2.0, 0)  # Centro de la tapa superior
    for i in range(slices + 1):
        angle = 2.0 * math.pi * float(i) / float(slices)
        x = radius * math.cos(angle)
        z = radius * math.sin(angle)
        glVertex3f(x, height / 2.0, z)
    glEnd()

    glBegin(GL_TRIANGLE_FAN)
    glNormal3f(0, -1, 0)
    glVertex3f(0, -height / 2.0, 0)  # Centro de la tapa inferior
    for i in range(slices + 1):
        angle = 2.0 * math.pi * float(i) / float(slices)
        x = radius * math.cos(angle)
        z = radius * math.sin(angle)
        glVertex3f(x, -height / 2.0, z)
    glEnd()

    glPopMatrix()

def draw_sphere(radius, slices, stacks):
    for i in range(stacks):
        lat0 = math.pi * (-0.5 + float(i) / stacks)
        z0 = radius * math.sin(lat0)
        zr0 = radius * math.cos(lat0)

        lat1 = math.pi * (-0.5 + float(i + 1) / stacks)
        z1 = radius * math.sin(lat1)
        zr1 = radius * math.cos(lat1)

        glBegin(GL_QUAD_STRIP)
        for j in range(slices + 1):
            lng = 2 * math.pi * float(j - 1) / slices
            x = math.cos(lng)
            y = math.sin(lng)

            glNormal3f(x * zr0, y * zr0, z0)
            glVertex3f(x * zr0, y * zr0, z0)
            glNormal3f(x * zr1, y * zr1, z1)
            glVertex3f(x * zr1, y * zr1, z1)
        glEnd()

    glPopMatrix()

def draw_cone(pos_x, pos_y, pos_z, radius, height):
    glPushMatrix()
    glTranslatef(pos_x, pos_y, pos_z)
    glRotatef(-90, 1.0, 0.0, 0.0)
    glutSolidCone(radius, height, 20, 20)
    glPopMatrix()    
