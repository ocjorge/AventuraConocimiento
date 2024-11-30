#draw.py
import pygame
import numpy as np
import math
import os
import random
import OpenGL.GL as gl
from OpenGL.GLU import *
from OpenGL.GL import *
from OpenGL.GLUT import *
from pygame.locals import *
from PIL import *
from . import iluminacion as lc
from . import objetos as obj
from .posiciones import *
from .colors import *
from .character import *
from .billy import *
from .enemy import *
from .posiciones import *

posi = GamePositions()
# Dibuja el personaje y aplica iluminación
def draw_character(personaje, pos_x, pos_y, pos_z):
    glEnable(GL_DEPTH_TEST)
    glPushMatrix()
    glTranslatef(pos_x, pos_y, pos_z)
    personaje.draw()
    glPopMatrix()
    glDisable(GL_LIGHTING)
    glDisable(GL_LIGHT0)

def drawPerfumin(character):
    glEnable(GL_DEPTH_TEST)
    glPushMatrix()
    glTranslatef(posi.PosX_objeto1, posi.PosY_objeto1, posi.PosZ_objeto1)
    character.draw()  # Llama al método `draw()` del personaje
    glPopMatrix()
    glDisable(GL_LIGHTING)
    glDisable(GL_LIGHT0)

def drawBilly(snowman):
    glEnable(GL_DEPTH_TEST)
    glPushMatrix()
    glTranslatef(posi.PosX_objeto11, posi.PosY_objeto11, posi.PosZ_objeto11)
    snowman.draw()  # Llama al método `draw()` del personaje
    glPopMatrix()
    glDisable(GL_LIGHTING)
    glDisable(GL_LIGHT0)

def drawEnemy(enemy):
    glEnable(GL_DEPTH_TEST)
    glPushMatrix()
    glTranslatef(posi.PosX_objeto21, posi.PosY_objeto21, posi.PosZ_objeto21)
    enemy.draw()  # Llama al método `draw()` del personaje
    glPopMatrix()
    glDisable(GL_LIGHTING)
    glDisable(GL_LIGHT0)

def draw2(movX, movY):
    global PosX_objeto2, PosY_objeto2
    PosX_objeto2 += movX
    PosY_objeto2 += movY

    glEnable(GL_DEPTH_TEST)
    glPushMatrix()
    glTranslatef(posi.PosX_objeto2, posi.PosY_objeto2, posi.PosZ_objeto2)
    lc.phong(0.3, 0.6, 0.1)
    lc.gouraud(255.0, 200.0, 150.0)
    obj.draw_cube_dos()
    glPopMatrix()
    glDisable(GL_LIGHTING)
    glDisable(GL_LIGHT0)

def draw3(movX, movY):
    global PosX_objeto3, PosY_objeto3
    PosX_objeto3 += movX
    PosY_objeto3 += movY

    glEnable(GL_DEPTH_TEST)
    glPushMatrix()
    glTranslatef(posi.PosX_objeto3, posi.PosY_objeto3, posi.PosZ_objeto3)
    lc.interpolado(255.0, 255.0, 255.0)
    obj.draw_cube()
    glPopMatrix()
    glDisable(GL_LIGHTING)
    glDisable(GL_LIGHT0)

def draw4(movX, movY):
    global PosX_objeto4, PosY_objeto4, objeto4_size
    PosX_objeto4 += movX
    PosY_objeto4 += movY

    glEnable(GL_DEPTH_TEST)
    glPushMatrix()
    glTranslatef(posi.PosX_objeto4, posi.PosY_objeto4, posi.PosZ_objeto4)
    lc.interpolado(255.0, 165.0, 0.0)
    obj.draw_pyramid(3, 6, 0, 4)
    glPopMatrix()
    glDisable(GL_LIGHTING)
    glDisable(GL_LIGHT0)

def draw5(movX, movY):
    global PosX_objeto5, PosY_objeto5, objeto5_radius, objeto5_height
    PosX_objeto5 += movX
    PosY_objeto5 += movY

    glEnable(GL_DEPTH_TEST)
    glPushMatrix()
    glTranslatef(posi.PosX_objeto5, posi.PosY_objeto5, posi.PosZ_objeto5)
    lc.gouraud(128.0, 0.0, 128.0)
    obj.draw_cylinder(0, 0, 0, 2, 5)
    glPopMatrix()
    glDisable(GL_LIGHTING)
    glDisable(GL_LIGHT0)

def draw_malingo(position):
    glEnable(GL_DEPTH_TEST)
    glPushMatrix()
    glTranslatef(position[0], position[1], position[2])
    lc.interpolado(255.0, 165.0, 0.0)
    obj.draw_pyramid(3, 6, 0, 4)
    glPopMatrix()
    glDisable(GL_LIGHTING)
    glDisable(GL_LIGHT0)

def draw_collectible(posX, posY, posZ, rotation):
    glEnable(GL_DEPTH_TEST)
    glPushMatrix()
    glTranslatef(posX, posY, posZ)
    glRotatef(rotation, 0, 1, 0)
    
    lc.interpolado(255.0, 165.0, 0.0)
    
    obj.draw_pyramid(3, 6, 0, 4)
    glPopMatrix()
    glDisable(GL_LIGHTING)
    glDisable(GL_LIGHT0)

def draw_tesoro(position):
    glEnable(GL_DEPTH_TEST)
    glPushMatrix()
    glTranslatef(position[0], position[1], position[2])
    lc.gouraud(128.0, 0.0, 128.0)
    obj.draw_cylinder(0, 0, 0, 2, 5)
    glPopMatrix()
    glDisable(GL_LIGHTING)
    glDisable(GL_LIGHT0)

# Dibuja los malos
def draw_malos_uno():
    gl.glEnable(gl.GL_DEPTH_TEST)
    gl.glPushMatrix()
    
    # Generar posiciones aleatorias en un rango de -20 a 20
    posiciones = [
        (random.uniform(-20, 20), 
         random.uniform(-20, 20), 
         random.uniform(-20, 20)) 
        for _ in range(4)
    ]
    
    # Colores RGB aleatorios
    colores = [
        (random.random(), random.random(), random.random()) 
        for _ in range(4)
    ]
    
    # Dibujar cilindros en posiciones aleatorias
    for (x, y, z), color in zip(posiciones, colores):
        gl.glPushMatrix()
        gl.glTranslatef(x, y, z)
        gl.glColor3f(*color)  # Establece el color aleatorio antes de dibujar
        obj.draw_cylinder(0, 0, 0, 2, 5)
        gl.glPopMatrix()
    
    gl.glPopMatrix()
    
def draw_malos_dos():
    gl.glEnable(gl.GL_DEPTH_TEST)
    gl.glPushMatrix()
    
    # Generar 8 posiciones aleatorias en un rango de -20 a 20
    posiciones = [
        (random.uniform(-20, 20), 
         random.uniform(-20, 20), 
         random.uniform(-20, 20)) 
        for _ in range(8)
    ]
    
    # Colores RGB aleatorios para 8 cilindros
    colores = [
        (random.random(), random.random(), random.random()) 
        for _ in range(8)
    ]
    
    # Dibujar cilindros en posiciones aleatorias
    for (x, y, z), color in zip(posiciones, colores):
        gl.glPushMatrix()
        gl.glTranslatef(x, y, z)
        gl.glColor3f(*color)
        obj.draw_pyramid(3, 6, 0, 4)
        gl.glPopMatrix()
    
    gl.glPopMatrix()

def draw_malos_tres():
    gl.glEnable(gl.GL_DEPTH_TEST)
    gl.glPushMatrix()
    
    # Generar 12 posiciones aleatorias en un rango de -20 a 20
    posiciones = [
        (random.uniform(-20, 20), 
         random.uniform(-20, 20), 
         random.uniform(-20, 20)) 
        for _ in range(12)
    ]
    
    # Colores RGB aleatorios para 12 cilindros
    colores = [
        (random.random(), random.random(), random.random()) 
        for _ in range(12)
    ]
    
    # Dibujar cilindros en posiciones aleatorias
    for (x, y, z), color in zip(posiciones, colores):
        gl.glPushMatrix()
        gl.glTranslatef(x, y, z)
        gl.glColor3f(*color)
        obj.draw_sphere(2, 5, 5)
        gl.glPopMatrix()
    
    gl.glPopMatrix()



