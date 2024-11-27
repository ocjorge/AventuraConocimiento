# character.py
import math
import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
from .objetos import *
from .colors import *
from .shapes import *
import math

directorio_script = os.path.dirname(os.path.abspath(__file__))

class Character:
    def __init__(self):
        self.position = [0, 0, 0]
        self.rotation = [0, 0, 0]
        self.scale = [4, 4, 4]
        self.walk_cycle = 0
        self.jump_cycle = 0  
        self.jump_height = 0
        self.is_jumping = False
        self.is_crouching = False
        self.is_lying = False
        self.kick_angle = 0
        self.expression = 'neutral'
        self.left_arm_angle = 0
        self.right_arm_angle = 0
        self.left_leg_angle = 0
        self.right_leg_angle = 0
        self.crouch_start_time = 0
        self.crouch_duration = 1000  # duración en milisegundos
        self.is_crouching = False
        self.visible = True
        self.collision_info = {
            'x': 0, 'y': 0, 'z': 0,
            'width': 1, 'height': 2, 'depth': 1  # Ajusta estos valores según el tamaño de tu personaje
        }

    def update_collision_info(self):
        self.x = self.position[0]
        self.y = self.position[1]
        self.z = self.position[2]
        self.width = self.scale[0]
        self.height = self.scale[1]
        self.depth = self.scale[2]

    def set_expression(self, expression):
        self.expression = expression

    def reset(self):
        self.__init__()


    def translate(self, x, y, z):
        self.position[0] += x
        self.position[1] += y
        self.position[2] += z

    def rotate(self, angle, x, y, z):
        self.rotation[0] += angle * x
        self.rotation[1] += angle * y
        self.rotation[2] += angle * z

    def scale(self, sx, sy, sz):
        self.scale[0] *= sx
        self.scale[1] *= sy
        self.scale[2] *= sz

    def walk(self):
        self.walk_cycle += 0.1
        if self.walk_cycle > math.pi * 2:
            self.walk_cycle = 0
        self.left_leg_angle = math.sin(self.walk_cycle) * 30
        self.right_leg_angle = math.sin(self.walk_cycle + math.pi) * 30
        self.left_arm_angle = math.sin(self.walk_cycle + math.pi) * 30
        self.right_arm_angle = math.sin(self.walk_cycle) * 30

    
    def jump(self):
        if not self.is_jumping:
            self.is_jumping = True
            self.jump_cycle = 0
        if self.is_jumping:
            self.jump_height = math.sin(self.jump_cycle) * 0.5
            self.jump_cycle += 0.1
            if self.jump_cycle > math.pi:
                self.jump_cycle = 0
                self.jump_height = 0
                self.is_jumping = False

    def crouch(self):
        self.is_crouching = not self.is_crouching

    def lie_down(self):
        self.is_lying = not self.is_lying

    def kick(self):
        self.kick_angle = 45
    
    def raise_left_arm(self):
        self.left_arm_angle = min(90, self.left_arm_angle + 5)

    def raise_right_arm(self):
        self.right_arm_angle = min(90, self.right_arm_angle + 5)

    def lower_arms(self):
        self.left_arm_angle = max(0, self.left_arm_angle - 5)
        self.right_arm_angle = max(0, self.right_arm_angle - 5)


    def draw_face(self):
        glColor3fv(ORANGE)
        
        # Ojos
        glPushMatrix()
        glTranslatef(-0.1, 0.1, 0.31)
        if self.expression in ['wink', 'fear']:
            glScalef(1, 0.1, 1)  # Ojo izquierdo cerrado o entrecerrado
        create_sphere(0.05, 10, 10)
        glPopMatrix()

        glPushMatrix()
        glTranslatef(0.1, 0.1, 0.31)
        if self.expression == 'wink':
            create_sphere(0.05, 10, 10)  # Ojo derecho abierto en guiño
        elif self.expression == 'fear':
            glScalef(1, 1.5, 1)  # Ojo derecho muy abierto en miedo
            create_sphere(0.05, 10, 10)
        else:
            create_sphere(0.05, 10, 10)
        glPopMatrix()


        # Boca
        glColor3fv(BLACK)
        glPushMatrix()
        glTranslatef(0, -0.1, 0.31)
        if self.expression in ['smile', 'interest']:
            glScalef(1, 0.5, 1)
            create_sphere(0.1, 10, 10)  # Sonrisa
        elif self.expression == 'sad':
            glRotatef(180, 1, 0, 0)
            glScalef(1, 0.5, 1)
            create_sphere(0.1, 10, 10)  # Boca triste
        elif self.expression == 'fear':
            glScalef(0.5, 1, 1)
            create_sphere(0.1, 10, 10)  # Boca de miedo (O)
        elif self.expression == 'angry':
            glScalef(1, 0.5, 1)
            create_sphere(0.05, 10, 10)  # Boca enojada
        elif self.expression == 'doubt':
            glScalef(0.7, 0.3, 1)
            glTranslatef(0.05, 0, 0)
            create_sphere(0.1, 10, 10)  # Boca de duda
        elif self.expression == 'admiration':
            glScalef(0.8, 0.8, 1)
            create_sphere(0.1, 10, 10)  # Boca de admiración
        else:
            glScalef(1, 0.2, 1)
            create_sphere(0.1, 10, 10)  # Boca neutral
        glPopMatrix()

        # Cejas (para algunas expresiones)
        if self.expression in ['angry', 'interest', 'doubt', 'admiration']:
            glColor3fv(BLACK)
            glPushMatrix()
            glTranslatef(-0.1, 0.2, 0.31)
            if self.expression == 'angry':
                glRotatef(30, 0, 0, 1)
            elif self.expression == 'interest':
                glRotatef(-30, 0, 0, 1)
            elif self.expression == 'doubt':
                glRotatef(15, 0, 0, 1)
            elif self.expression == 'admiration':
                glRotatef(-45, 0, 0, 1)
            glScalef(0.1, 0.02, 0.02)
            self.draw_cube(1)  
            glPopMatrix()

            glPushMatrix()
            glTranslatef(0.1, 0.2, 0.31)
            if self.expression == 'angry':
                glRotatef(-30, 0, 0, 1)
            elif self.expression == 'interest':
                glRotatef(30, 0, 0, 1)
            elif self.expression == 'doubt':
                glRotatef(-15, 0, 0, 1)
            elif self.expression == 'admiration':
                glRotatef(45, 0, 0, 1)
            glScalef(0.1, 0.02, 0.02)
            self.draw_cube(1)  
            glPopMatrix()
    
    def draw_cube(self, size):
        glBegin(GL_QUADS)
        # Front face
        glVertex3f(-size/2, -size/2,  size/2)
        glVertex3f( size/2, -size/2,  size/2)
        glVertex3f( size/2,  size/2,  size/2)
        glVertex3f(-size/2,  size/2,  size/2)
        # Back face
        glVertex3f(-size/2, -size/2, -size/2)
        glVertex3f(-size/2,  size/2, -size/2)
        glVertex3f( size/2,  size/2, -size/2)
        glVertex3f( size/2, -size/2, -size/2)
        # Top face
        glVertex3f(-size/2,  size/2, -size/2)
        glVertex3f(-size/2,  size/2,  size/2)
        glVertex3f( size/2,  size/2,  size/2)
        glVertex3f( size/2,  size/2, -size/2)
        # Bottom face
        glVertex3f(-size/2, -size/2, -size/2)
        glVertex3f( size/2, -size/2, -size/2)
        glVertex3f( size/2, -size/2,  size/2)
        glVertex3f(-size/2, -size/2,  size/2)
        # Right face
        glVertex3f( size/2, -size/2, -size/2)
        glVertex3f( size/2,  size/2, -size/2)
        glVertex3f( size/2,  size/2,  size/2)
        glVertex3f( size/2, -size/2,  size/2)
        # Left face
        glVertex3f(-size/2, -size/2, -size/2)
        glVertex3f(-size/2, -size/2,  size/2)
        glVertex3f(-size/2,  size/2,  size/2)
        glVertex3f(-size/2,  size/2, -size/2)
        glEnd()
        
    def draw(self):
        # Si el personaje no está activo, no lo dibuja
        if not getattr(self, 'is_active', True):
          return
        
        glPushMatrix()
        
        # Aplicar transformaciones
        glTranslatef(*self.position)
        glTranslatef(0, self.jump_height, 0)
        glRotatef(self.rotation[0], 1, 0, 0)
        glRotatef(self.rotation[1], 0, 1, 0)
        glRotatef(self.rotation[2], 0, 0, 1)
        glScalef(*self.scale)

        if self.is_lying:
            glRotatef(90, 0, 0, 1)

        # Cuerpo
        glColor3fv(BLUE)
        if self.is_crouching:
            create_cube(0, -0.25, 0, 0.5)
        else:
            create_cube(0, 0, 0, 0.5)
        
        # Cabeza
        glColor3fv(RED)
        if self.is_crouching:
            create_cube(0, 0.75, 0, 0.3)
        else:
            create_cube(0, 1, 0, 0.3)
        
        # Dibujar la cara
        self.draw_face()
        
        # Cuello
        glColor3fv(GREEN)
        if self.is_crouching:
            create_cube(0, 0.35, 0, 0.1)
        else:
            create_cube(0, 0.6, 0, 0.1)
        
        # Brazos
        glColor3fv(YELLOW)
        glPushMatrix()
        glTranslatef(-0.7, 0, 0)
        glRotatef(self.left_arm_angle, 1, 0, 0)
        create_cube(0, 0, 0, 0.2)
        glPopMatrix()

        glPushMatrix()
        glTranslatef(0.7, 0, 0)
        glRotatef(self.right_arm_angle, 1, 0, 0)
        create_cube(0, 0, 0, 0.2)
        glPopMatrix()
        
        # Piernas
        glColor3fv(PURPLE)
        leg_y = -1 if not self.is_crouching else -0.75
        left_leg_angle = math.sin(self.walk_cycle) * 30
        right_leg_angle = math.sin(self.walk_cycle + math.pi) * 30

        # Pierna izquierda
        glPushMatrix()
        glTranslatef(-0.3, leg_y, 0)
        glRotatef(left_leg_angle, 1, 0, 0)
        create_cube(0, 0, 0, 0.2)
        glPopMatrix()

        # Pierna derecha (con opción de patada)
        glPushMatrix()
        glTranslatef(0.3, leg_y, 0)
        if self.kick_angle > 0:
            glRotatef(-self.kick_angle, 1, 0, 0)
            self.kick_angle = max(0, self.kick_angle - 5)
        else:
            glRotatef(right_leg_angle, 1, 0, 0)
        create_cube(0, 0, 0, 0.2)
        glPopMatrix()

        glPopMatrix()

    def wave_arm(self, time):
        angle = math.sin(time) * 45
        glPushMatrix()
        glTranslatef(0.7, 0, 0)
        glRotatef(angle, 0, 0, 1)
        glColor3fv(YELLOW)
        create_cube(0, 0, 0, 0.2)
        glPopMatrix()
    
    def remove(self):
        # Marca al personaje como eliminado visualmente
        self.is_active = False



create_character = Character()
# Ejemplo de uso:
# En el bucle principal del juego:
# create_character.walk()
# create_character.jump()
# create_character.crouch()
# create_character.lie_down()
# create_character.kick()
# create_character.set_expression('smile')  # Cambiar la expresión
# create_character.draw()

