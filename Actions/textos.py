#textos.py
import pygame
from OpenGL.GL import *
from OpenGL.GLU import *

def draw_text(text, PosX, PosY, PosZ, sizeFont, R, G, B, RB, GB, BB):
    font = pygame.font.Font(None, sizeFont)
    text_surface = font.render(text, True, (R, G, B), (RB, GB, BB))  # características de texto
    text_data = pygame.image.tostring(text_surface, "RGBA", True)
    
    glRasterPos3d(PosX, PosY, PosZ)
    glDrawPixels(text_surface.get_width(), 
                 text_surface.get_height(), 
                 GL_RGBA, GL_UNSIGNED_BYTE, text_data)

def create_text_texture(text, sizeFont, R, G, B, RB, GB, BB):
    """Crea una textura a partir del texto"""
    font = pygame.font.Font(None, sizeFont)
    text_surface = font.render(text, True, (R, G, B), (RB, GB, BB))
    text_data = pygame.image.tostring(text_surface, "RGBA", True)
    
    # Crear la textura
    texture = glGenTextures(1)
    glBindTexture(GL_TEXTURE_2D, texture)
    
    # Configurar parámetros de la textura
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)
    
    # Cargar los datos de la textura
    glTexImage2D(GL_TEXTURE_2D, 0, GL_RGBA, text_surface.get_width(), text_surface.get_height(),
                 0, GL_RGBA, GL_UNSIGNED_BYTE, text_data)
    
    return texture, text_surface.get_width(), text_surface.get_height()

def draw_text_3d(text, PosX, PosY, PosZ, sizeFont, R, G, B, RB, GB, BB):
    """Dibuja texto 3D utilizando glRasterPos3d"""
    font = pygame.font.Font(None, sizeFont)
    text_surface = font.render(text, True, (R, G, B), (RB, GB, BB))
    text_data = pygame.image.tostring(text_surface, "RGBA", True)

    glRasterPos3d(PosX, PosY, PosZ)
    glDrawPixels(text_surface.get_width(),
                 text_surface.get_height(),
                 GL_RGBA, GL_UNSIGNED_BYTE, text_data)