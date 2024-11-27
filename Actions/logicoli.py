#logicoli.py
import pygame
import numpy as np
import math
import os
from OpenGL.GLU import *
from OpenGL.GL import *
from OpenGL.GLUT import *
from pygame.locals import *
from PIL import *
from . import colisiones as coli
from . import objetos as obj
from .posiciones import *  
from . import draw as drw
from . import textos as txt
from .preguntas import JuegoPreguntas
from .posiciones import GamePositions as posi
from .posiciones import game_positions
from .character import create_character
from .enemy import create_enemy
from .billy import Snowman


class LogicaColision:
    def __init__(self):
        
        self.lives = 3

        self.positions = game_positions

        self.character = create_character
        self.enemy = create_enemy
        self.snowman = Snowman()
        self.selected_character = None
        self.score = 0
        
        self.positions = game_positions

        self.player_positions = {
            1: [0, 0, 0],  # Posición inicial del personaje 1
            2: [0, 0, 0],  # Posición inicial del personaje 2
            3: [0, 0, 0]   # Posición inicial del personaje 3
        }

      
    def get_player_position(self, action):
        """
        Obtiene la posición actual del jugador basado en la acción o personaje seleccionado
        Returns: [PosX, PosY, PosZ]
        """
        if action in [1, 2, 3]:
            return self.positions.get_character_position(action)
        return self.positions.get_character_position(self.selected_character)

    def get_player_coordinates(self, action):
        """
        Obtiene las coordenadas del jugador basado en la acción o personaje seleccionado
        Returns: (player_pos_x, player_pos_y, player_pos_z)
        """
        player_position = self.get_player_position(action)
        player_pos_x, player_pos_y, player_pos_z = player_position
        return player_pos_x, player_pos_y, player_pos_z
    
    def update_position(self, selected_character, new_x, new_y, new_z):
        """Actualiza la posición del personaje seleccionado."""
        if selected_character == 1:
            self.positions.PosX_objeto1 = new_x
            self.positions.PosY_objeto1 = new_y
            self.positions.PosZ_objeto1 = new_z
        elif selected_character == 2:
            self.positions.PosX_objeto11 = new_x
            self.positions.PosY_objeto11 = new_y
            self.positions.PosZ_objeto11 = new_z
        elif selected_character == 3:
            self.positions.PosX_objeto21 = new_x
            self.positions.PosY_objeto21 = new_y
            self.positions.PosZ_objeto21 = new_z

    def colisiones_malo_uno(self, action):
        # Obtenemos la posición actual del jugador
        player_pos_x, player_pos_y, player_pos_z = self.get_player_coordinates(action)

        if coli.rombo_collision(
            self.positions.PosX_objeto2,
            self.positions.PosY_objeto2,
            self.positions.PosZ_objeto2,
            self.positions.objeto2_width,
            self.positions.objeto2_height,
            self.positions.objeto2_depth,
            player_pos_x,
            player_pos_y,
            player_pos_z,
            self.positions.objeto1_height
        ):
            return True


        if coli.rombo_collision(
            self.positions.PosX_objeto4,
            self.positions.PosY_objeto4,
            self.positions.PosZ_objeto4,
            self.positions.objeto4_width,
            self.positions.objeto4_height,
            self.positions.objeto4_depth,
            player_pos_x,
            player_pos_y,
            player_pos_z,
            self.positions.objeto1_height
        ):
            return True

        if coli.rombo_collision(
            self.positions.PosX_objeto6,
            self.positions.PosY_objeto6,
            self.positions.PosZ_objeto6,
            self.positions.objeto6_width,
            self.positions.objeto6_height,
            self.positions.objeto6_depth,
            player_pos_x,
            player_pos_y,
            player_pos_z,
            self.positions.objeto1_height
        ):
            return True
        
        if coli.rombo_collision(
            self.positions.PosX_objeto8,
            self.positions.PosY_objeto8,
            self.positions.PosZ_objeto8,
            self.positions.objeto8_width,
            self.positions.objeto8_height,
            self.positions.objeto8_depth,
            player_pos_x,
            player_pos_y,
            player_pos_z,
            self.positions.objeto1_height
        ):
            return True

        if coli.rombo_collision(
            self.positions.PosX_objeto10,
            self.positions.PosY_objeto10,
            self.positions.PosZ_objeto10,
            self.positions.objeto10_width,
            self.positions.objeto10_height,
            self.positions.objeto10_depth,
            player_pos_x,
            player_pos_y,
            player_pos_z,
            self.positions.objeto1_height
        ):
            return True 

    def colisiones_bueno_uno(self, action):
         # Obtenemos la posición actual del jugador
        player_pos_x, player_pos_y, player_pos_z = self.get_player_coordinates(action)

        if coli.rombo_collision(
            self.positions.PosX_objeto16,
            self.positions.PosY_objeto16,
            self.positions.PosZ_objeto16,
            self.positions.objeto16_width,
            self.positions.objeto16_height,
            self.positions.objeto16_depth,
            player_pos_x,
            player_pos_y,
            player_pos_z,
            self.positions.objeto1_height
        ):
            return True
      

        if coli.rombo_collision(
            self.positions.PosX_objeto18,
            self.positions.PosY_objeto18,
            self.positions.PosZ_objeto18,
            self.positions.objeto18_width,
            self.positions.objeto18_height,
            self.positions.objeto18_depth,
            player_pos_x,
            player_pos_y,
            player_pos_z,
            self.positions.objeto1_height
        ):
            return True

        if coli.rombo_collision(
            self.positions.PosX_objeto6,
            self.positions.PosY_objeto6,
            self.positions.PosZ_objeto6,
            self.positions.objeto6_width,
            self.positions.objeto6_height,
            self.positions.objeto6_depth,
            player_pos_x,
            player_pos_y,
            player_pos_z,
            self.positions.objeto1_height
        ):
            return True
        
        if coli.rombo_collision(
            self.positions.PosX_objeto8,
            self.positions.PosY_objeto8,
            self.positions.PosZ_objeto8,
            self.positions.objeto8_width,
            self.positions.objeto8_height,
            self.positions.objeto8_depth,
            player_pos_x,
            player_pos_y,
            player_pos_z,
            self.positions.obobjeto1_height
        ):
            return True