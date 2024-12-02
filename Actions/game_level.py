#game_level.py
from OpenGL.GL import *
from OpenGL.GLUT import *
from enum import Enum
import logging
from enum import Enum
from typing import List, Optional
from dataclasses import dataclass
import random
import pygame
import math
from . import posiciones as posi
from . import sonidos as son
from . import draw as draw
from . import escenarios as es
from . import character as char
from . import logicoli
from .logicoli import LogicaColision as logicoli
from .character import create_character
from . import enemy as enemy
from .enemy import create_enemy
from . import billy as billy
from .billy import Snowman
from .preguntas import JuegoPreguntas
from .logicoli import LogicaColision
from . import textos as textos
from .posiciones import game_positions
from . import game_state_manager
from .game_state_manager import GameStateManager, GameStatus
from . import diccionario
from .diccionario import ventana_diccionario    

character = create_character  # Usamos la instancia importada
enemy = create_enemy
snowman = Snowman()
action_number = 0
posi = game_positions
selected_character = 0
game_state_manager = GameStateManager()
VENTANA = False

# Configuración del logging
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    filename='game_debug.log'
)
logger = logging.getLogger('GameLevel')

# Estados del juego y animaciones
class GameState(Enum):
    MAIN_MENU = "main_menu"
    PLAYING = "playing"
    PAUSED = "paused"
    GAME_OVER = "game_over"
    LEVEL_COMPLETE = "level_complete"
    TITLE_SCREEN = 1
    CHARACTER_SELECT = 2
    PLAYING_LEVEL = 3
    ANSWERING_QUESTION = "answering_question"

class AnimationState(Enum):
    IDLE = "idle"
    WALKING = "walking"
    JUMPING = "jumping"
    CROUCHING = "crouching"
    KICKING = "kicking"

# Clase para los límites del mapa
@dataclass
class MapBoundaries:
    min_x: float = -100.0
    max_x: float = 100.0
    min_y: float = 0.0
    max_y: float = 50.0
    min_z: float = -100.0
    max_z: float = 100.0

# Observer para colisiones
class CollisionObserver:
    def __init__(self):
        self._observers: List[callable] = []
    
    def attach(self, observer: callable):
        self._observers.append(observer)
        logger.debug(f"Observer attached: {observer.__name__}")
    
    def detach(self, observer: callable):
        self._observers.remove(observer)
        logger.debug(f"Observer detached: {observer.__name__}")
    
    def notify(self, entity_a, entity_b, collision_type: str):
        for observer in self._observers:
            observer(entity_a, entity_b, collision_type)

class GameLevel:
    def __init__(self):
        self.DEBUG_MODE = False
        # Configuración inicial del juego
        self.selected_character = None
        self.level_number = 1
        self.score = 0
        self.high_score = 0
        self.game_over = False
        self.lives = 3
        self.correct_answers = 0
        self.wrong_answers = 0
        
        self.logica_colision = LogicaColision()
        self.juego_preguntas = JuegoPreguntas(on_success=self.on_question_success, on_failure=self.on_question_failure)

        self.character = create_character
        self.enemy = create_enemy
        self.snowman = Snowman()
        self.selected_character = None

        

        # Configuración de niveles
        self.level_configs = {
            1: {"required_correct_answers": 3, "enemies": 5, "treasures": 5},
            2: {"required_correct_answers": 3, "enemies": 5, "treasures": 5},
            3: {"required_correct_answers": 3, "enemies": 5, "treasures": 5}
        }


        self.collision_margin = 1.0  # Margen de colisión ajustable
        self.current_level = self.level_configs[1]

        # Lista de escenarios y sonidos
        self.escenarios = [
            "Fondos/01.jpg", "Fondos/02.jpg", "Fondos/03.jpeg",
            "Fondos/04.jpeg", "Fondos/05.jpg", "Fondos/06.jpeg",
            "Fondos/07.jpeg", "Fondos/08.jpg", "Fondos/09.jpeg",
            "Fondos/10.jpg", "Fondos/11.jpg", "Fondos/12.jpg",
            "Fondos/13.jpg", "Fondos/14.jpg", "Fondos/15.jpg"
        ]
        self.current_escenario = 0

    def on_question_success(self):
        self.advance_level()

    def on_question_failure(self):
        self.game_state = GameState.GAME_OVER
        logger.info("Game Over - Fallaste 2 preguntas")
        self.game_over = True
    
    def update(self):
        """Actualiza el estado general del juego en cada cuadro."""
        if self.game_over:
            return
        
        self.handle_collision()
       

    def handle_collision(self):
        LogicaColision.colisiones_bueno_uno = False
        LogicaColision.colisiones_malo_uno = False
        
        if self.level_number == 1:
            self.score = 0
            self.correct_answers = 0
            self.wrong_answers = 0
            self.lives = 3
            #self.handle_question()
            if LogicaColision.colisiones_malo_uno:
                self.lives -= 1
                LogicaColision.colisiones_malo_uno = False
                self.handle_game_over()
            if LogicaColision.colisiones_bueno_uno:
                self.juego_preguntas.generar_pregunta()
                if self.juego_preguntas.respuestas_correctas:
                    self.correct_answers += 1
                    self.score += 100
                else:
                    self.wrong_answers += 1
                    self.lives -= 1 
                    self.handle_game_over()
        if self.level_number == 2:
            self.score = 0
            self.correct_answers = 0
            self.wrong_answers = 0
            self.lives = 3
            #self.handle_question()
            if LogicaColision.colisiones_malo_uno:
                self.lives -= 1
                LogicaColision.colisiones_malo_uno = False
                self.handle_game_over()
            if LogicaColision.colisiones_bueno_uno:
                self.juego_preguntas.generar_pregunta()
                if self.juego_preguntas.respuesta_correcta:
                    self.correct_answers += 1
                    self.score += 100                    
                else:
                    self.wrong_answers += 1
                    self.lives -= 1 
                    self.handle_game_over()
        if self.level_number == 2:
            self.score = 0
            self.correct_answers = 0
            self.wrong_answers = 0
            self.lives = 3
            #self.handle_question()
            if LogicaColision.colisiones_malo_uno:
                self.lives -= 1
                LogicaColision.colisiones_malo_uno = False
                self.handle_game_over()
            if LogicaColision.colisiones_bueno_uno:
                self.juego_preguntas.generar_pregunta()
                if self.juego_preguntas.respuesta_correcta:
                    self.correct_answers += 1
                    self.score += 100                    
                else:
                    self.wrong_answers += 1
                    self.lives -= 1 
                    self.handle_game_over()
                    
    def handle_question(self): 
        self.game_state = GameState.ANSWERING_QUESTION

        def on_question_complete(correct: bool):
            if correct:
                self.correct_answers += 1
                self.score += 100
                logger.info(f"Respuesta correcta - Total correctas: {self.correct_answers}")
            else:
                self.wrong_answers += 1
                logger.info(f"Respuesta incorrecta - Total incorrectas: {self.wrong_answers}")

            # Verificar progreso del nivel
            if self.correct_answers >= self.current_level["required_correct_answers"]:
                self.advance_level()
            elif self.wrong_answers >= 2:
                self.game_state = GameState.GAME_OVER
            else:
                self.game_state = GameState.PLAYING

          
    def handle_game_over(self):
        if self.lives == 0:
           self.game_state = GameState.GAME_OVER
           self.game_over = True   
        

    def advance_level(self):
        """Avanza al siguiente nivel o completa el juego."""
        if self.level_number < 3:
            self.level_number += 1
            self.current_level = self.level_configs[self.level_number]
            self.initialize_level(self.selected_character)
            logger.info(f"Avanzando al nivel {self.level_number}")
        else:
            self.game_state = GameState.LEVEL_COMPLETE
            logger.info("¡Juego completado!")    

    def generate_enemies_and_treasures(self):
        """Genera enemigos y tesoros en posiciones aleatorias."""

        self.level_number = game_state_manager.current_level    

        if self.level_number == 1:
            draw.draw_malos_uno()
            
        elif self.level_number == 2:
            draw.draw_malos_dos()
            
        elif self.level_number == 3:
            draw.draw_malos_tres()
            
     
    

    def draw_level(self, action):
        """Dibuja los elementos del nivel, incluyendo el personaje y enemigos."""

        glPushMatrix()
        # Dibujar el escenario con la textura del fondo
        
        glPopMatrix()

        # Configurar la iluminación
        glEnable(GL_LIGHTING)
        glEnable(GL_LIGHT0)
        glLightfv(GL_LIGHT0, GL_POSITION, [0, 50, 0, 1])  # Luz desde arriba
        glLightfv(GL_LIGHT0, GL_AMBIENT, [0.2, 0.2, 0.2, 1.0])
        glLightfv(GL_LIGHT0, GL_DIFFUSE, [1.0, 1.0, 1.0, 1.0])

        # Dibujar los personajes
        glPushMatrix()
        if action == 1:
            create_character.is_active = True
            glTranslatef(posi.PosX_objeto1, posi.PosY_objeto1, posi.PosZ_objeto1)
            self.character.draw()
            
        elif action == 2:
            snowman.visible = True
            glTranslatef(posi.PosX_objeto11, posi.PosY_objeto11, posi.PosZ_objeto11)
            self.snowman.draw()
            
        elif action == 3:
            enemy.is_visible = True
            glTranslatef(posi.PosX_objeto21, posi.PosY_objeto21, posi.PosZ_objeto21)
            self.enemy.draw()
           
        glPopMatrix()

        self.generate_enemies_and_treasures()

        enemy.is_visible = True
        character.is_active = True
        snowman.visible = True  
      
        # Dibujar el HUD
        #self.draw_hud()
       

    def initialize_level(self, action):
        """Inicializa el nivel con el personaje seleccionado."""
        self.selected_character = action
        # Resetear posición inicial según el personaje
        if action == 1:
            posi.PosX_objeto1, posi.PosY_objeto1, posi.PosZ_objeto1 = (0, 0, 0)
        elif action == 2:
            posi.PosX_objeto11, posi.PosY_objeto11, posi.PosZ_objeto11 = (0, 0, 0)
        elif action == 3:
            posi.PosX_objeto21, posi.PosY_objeto21, posi.PosZ_objeto21 = (0, 0, 0)

        # Cambiar configuración del nivel
        self.current_level = self.level_configs[self.level_number]

        enemy.is_visible = True
        character.is_active = True
        snowman.visible = True 

        # Cambiar escenario y música
        global current_escenario
        current_escenario = (self.current_escenario + 1) % len(self.escenarios)
        son.play_music(f"Sounds/level_{self.level_number}.mp3")

        # Generar enemigos y tesoros
        self.generate_enemies_and_treasures()

        
       

    def handle_movement(self, keys, selected_character):
        """Gestiona el movimiento del personaje basado en las teclas presionadas."""

        movement_speed = 0.5
        jump_speed = 1.0  # Velocidad de subida y bajada

        # Actualizar self.selected_character con el parámetro recibido
        self.selected_character = selected_character
        current_pos = self.logica_colision.get_player_position(selected_character)
        new_x, new_y, new_z = current_pos
        # Movimiento en X (izquierda/derecha)
        if keys[pygame.K_LEFT]:
            if self.selected_character == 1:
                posi.PosX_objeto1 -= movement_speed  # Mover a la izquierda
                self.character.walk()
            elif self.selected_character == 2:
                posi.PosX_objeto11 -= movement_speed
                self.snowman.walk()
            elif self.selected_character == 3:
                posi.PosX_objeto21 -= movement_speed
                self.enemy.walk()

        if keys[pygame.K_RIGHT]:
            if self.selected_character == 1:
                posi.PosX_objeto1 += movement_speed  # Mover a la derecha
                self.character.walk()
            elif self.selected_character == 2:
                posi.PosX_objeto11 += movement_speed
                self.snowman.walk()
            elif self.selected_character == 3:
                posi.PosX_objeto21 += movement_speed
                self.enemy.walk()

        # Movimiento en Z (adelante/atrás)
        if keys[pygame.K_UP]:
            if self.selected_character == 1:
                posi.PosZ_objeto1 -= movement_speed  # Mover hacia adelante (reducir Z)
                self.character.walk()
            elif self.selected_character == 2:
                posi.PosZ_objeto11 -= movement_speed
                self.snowman.walk()
            elif self.selected_character == 3:
                posi.PosZ_objeto21 -= movement_speed
                self.enemy.walk()

        if keys[pygame.K_DOWN]:
            if self.selected_character == 1:
                posi.PosZ_objeto1 += movement_speed  # Mover hacia atrás (incrementar Z)
                self.character.walk()
            elif self.selected_character == 2:
                posi.PosZ_objeto11 += movement_speed
                self.snowman.walk()
            elif self.selected_character == 3:
                posi.PosZ_objeto21 += movement_speed
                self.enemy.walk()

        # Movimiento en Y (subir/bajar)
        if keys[pygame.K_SPACE]:
            if self.selected_character == 1:
                posi.PosY_objeto1 += jump_speed  # Subir
                self.character.jump()
            elif self.selected_character == 2:
                posi.PosY_objeto11 += jump_speed
                self.snowman.jump()
            elif self.selected_character == 3:
                posi.PosY_objeto21 += jump_speed
                self.enemy.jump()

        if keys[pygame.K_n]:
            if self.selected_character == 1:
                posi.PosY_objeto1 -= jump_speed  # Bajar
                self.character.crouch()
            elif self.selected_character == 2:
                posi.PosY_objeto11 -= jump_speed
                self.snowman.crouch()
            elif self.selected_character == 3:
                posi.PosY_objeto21 -= jump_speed
                self.enemy.crouch()
        if keys[pygame.K_k]:
            if self.selected_character == 1:
                self.character.kick()
            elif self.selected_character == 2:
                self.snowman.kick()
            elif self.selected_character == 3:
                self.enemy.kick()

        if keys[pygame.K_h]:
            if self.selected_character == 1:   
                self.character.raise_left_arm()
                self.character.raise_right_arm()
            elif self.selected_character == 2:
                self.snowman.wave()
            elif self.selected_character == 3:
                self.enemy.kick()
        

        if keys[pygame.K_0]:
            son.play_sound("Sounds/s02.mp3")
            VENTANA = True
            if VENTANA:
                pygame.mouse.set_visible(True)
                diccionario.ventana_diccionario()
            
            if self.selected_character == 1:
                self.character.jump()
            elif self.selected_character == 2:
                self.snowman.jump()
            elif self.selected_character == 3:
                self.enemy.jump()

              
            
        
        if keys[pygame.K_ESCAPE]:
            self.game_over = True
        
        if keys[pygame.K_LEFT]:
            new_x -= movement_speed
        if keys[pygame.K_RIGHT]:
            new_x += movement_speed
        if keys[pygame.K_UP]:
            new_z -= movement_speed
        if keys[pygame.K_DOWN]:
            new_z += movement_speed
        if keys[pygame.K_SPACE]:
            new_y += jump_speed
        if keys[pygame.K_n]:
            new_y -= jump_speed
        
        self.logica_colision.update_position(selected_character, new_x, new_y, new_z)


    def get_player_position(self):
        """Devuelve la posición del jugador actual usando LogicaColision."""
        return self.logica_colision.get_player_position(self.selected_character)
    
    

    def update_jump(self):
        """Actualiza el estado de salto del personaje."""
        if self.is_jumping:
            if self.selected_character == 1:
                posi.PosY_objeto1 = self.jump_height
            elif self.selected_character == 2:
                posi.PosY_objeto11 = self.jump_height
            elif self.selected_character == 3:
                posi.PosY_objeto21 = self.jump_height

            # Actualizar altura del salto
            self.jump_height += self.jump_speed
            if self.jump_height >= self.max_jump_height:
                self.jump_speed = -self.jump_speed  # Comenzar a caer
            elif self.jump_height <= 0:
                self.jump_height = 0
                self.jump_speed = 0.1  # Resetear velocidad de salto
                self.is_jumping = False

    def draw_hud(self):
        """Dibuja la interfaz de usuario."""
        glPushMatrix()
        glDisable(GL_LIGHTING)
        
        # Configuración de colores
        text_color = (255, 255, 255)  # Blanco
        background_color = (0, 0, 0)  # Negro
        font_size = 24
        base_x = -0.95  # Posición horizontal fija
        base_y = 0.9    # Posición inicial vertical (ajustada)
        line_spacing = 0.2  # Espaciado mayor entre líneas (ajustado)

        # Dibujar la información del HUD con posiciones ajustadas
        textos.draw_text(f"Nivel: {self.level_number}", base_x, base_y, 0, font_size, *text_color, *background_color)
        #textos.draw_text(f"Vidas: {self.lives}", base_x, base_y - line_spacing, 0, font_size, *text_color, *background_color)
        #textos.draw_text(f"Puntuación: {self.score}", base_x, base_y - 2 * line_spacing, 0, font_size, *text_color, *background_color)
        #textos.draw_text(
        #    f"Aciertos: {self.correct_answers}/{self.current_level['required_correct_answers']}",
        #    base_x, base_y - 3 * line_spacing, 0, font_size, *text_color, *background_color
        #)
        
        glEnable(GL_LIGHTING)
        glPopMatrix()


    
    def setup_lighting(self):
        """Configura la iluminación de la escena."""
        glEnable(GL_LIGHTING)
        glEnable(GL_LIGHT0)
        glLightfv(GL_LIGHT0, GL_POSITION, [0, 50, 0, 1])
        glLightfv(GL_LIGHT0, GL_AMBIENT, [0.2, 0.2, 0.2, 1.0])
        glLightfv(GL_LIGHT0, GL_DIFFUSE, [1.0, 1.0, 1.0, 1.0])

    def draw_selected_character(self, action):
        """Dibuja el personaje seleccionado."""
        glPushMatrix()
        if action == 1:
            glTranslatef(posi.PosX_objeto1, posi.PosY_objeto1, posi.PosZ_objeto1)
            self.character.draw()
        elif action == 2:
            glTranslatef(posi.PosX_objeto11, posi.PosY_objeto11, posi.PosZ_objeto11)
            self.snowman.draw()
        elif action == 3:
            glTranslatef(posi.PosX_objeto21, posi.PosY_objeto21, posi.PosZ_objeto21)
            self.enemy.draw()
        glPopMatrix()

    def clear_level_state(self):
        """Limpia el estado del nivel anterior."""
        # Resetear contadores específicos del nivel
        self.correct_answers = 0
        self.wrong_answers = 0
        self.lives = 3
    
    

    