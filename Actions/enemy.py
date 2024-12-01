import math
import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import os

class Enemy:
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
        self.is_visible = True  # Nuevo atributo para controlar la visibilidad
        self.colors = {
            'body': (0.4, 0.6, 0.8),  # Azul pastel
            'head': (0.9, 0.6, 0.6),  # Rosa suave
            'limbs': (0.7, 0.7, 0.9), # Lila suave
            'details': (0.3, 0.3, 0.3) # Gris oscuro
        }
        
    def draw_filled_cube(self, size):
        # [El resto del método se mantiene igual]
        vertices = [
            # Frente
            (-size/2, -size/2, size/2),
            (size/2, -size/2, size/2),
            (size/2, size/2, size/2),
            (-size/2, size/2, size/2),
            # Atrás
            (-size/2, -size/2, -size/2),
            (-size/2, size/2, -size/2),
            (size/2, size/2, -size/2),
            (size/2, -size/2, -size/2),
        ]
        
        surfaces = [
            [0, 1, 2, 3],  # Frente
            [4, 5, 6, 7],  # Atrás
            [1, 7, 6, 2],  # Derecha
            [4, 0, 3, 5],  # Izquierda
            [3, 2, 6, 5],  # Arriba
            [4, 7, 1, 0]   # Abajo
        ]
        
        normals = [
            [0, 0, 1],    # Frente
            [0, 0, -1],   # Atrás
            [1, 0, 0],    # Derecha
            [-1, 0, 0],   # Izquierda
            [0, 1, 0],    # Arriba
            [0, -1, 0]    # Abajo
        ]

        glBegin(GL_QUADS)
        for i, surface in enumerate(surfaces):
            glNormal3fv(normals[i])
            for vertex in surface:
                glVertex3fv(vertices[vertex])
        glEnd()

    def draw_filled_sphere(self, radius, slices, stacks):
        quadric = gluNewQuadric()
        gluQuadricNormals(quadric, GLU_SMOOTH)
        gluQuadricDrawStyle(quadric, GLU_FILL)
        gluSphere(quadric, radius, slices, stacks)
        gluDeleteQuadric(quadric)

    def draw_face(self):
        # [El resto del método se mantiene igual]
        # Configurar iluminación para la cara
        glEnable(GL_LIGHTING)
        glEnable(GL_LIGHT0)
        light_position = [5.0, 5.0, 5.0, 1.0]
        glLightfv(GL_LIGHT0, GL_POSITION, light_position)

        # Material para los ojos
        glMaterialfv(GL_FRONT, GL_AMBIENT, [0.2, 0.2, 0.2, 1.0])
        glMaterialfv(GL_FRONT, GL_DIFFUSE, [0.1, 0.1, 0.1, 1.0])
        glMaterialfv(GL_FRONT, GL_SPECULAR, [0.5, 0.5, 0.5, 1.0])
        glMaterialf(GL_FRONT, GL_SHININESS, 32.0)

        # Ojos
        glPushMatrix()
        glTranslatef(-0.1, 0.1, 0.31)
        if self.expression in ['wink', 'fear']:
            glScalef(1, 0.1, 1)
        self.draw_filled_sphere(0.05, 20, 20)
        glPopMatrix()

        glPushMatrix()
        glTranslatef(0.1, 0.1, 0.31)
        if self.expression == 'wink':
            self.draw_filled_sphere(0.05, 20, 20)
        elif self.expression == 'fear':
            glScalef(1, 1.5, 1)
            self.draw_filled_sphere(0.05, 20, 20)
        else:
            self.draw_filled_sphere(0.05, 20, 20)
        glPopMatrix()

        # Material para la boca
        glMaterialfv(GL_FRONT, GL_AMBIENT, [0.1, 0.1, 0.1, 1.0])
        glMaterialfv(GL_FRONT, GL_DIFFUSE, [0.2, 0.2, 0.2, 1.0])

        # Boca
        glPushMatrix()
        glTranslatef(0, -0.1, 0.31)
        if self.expression == 'smile':
            glScalef(1, 0.5, 1)
            self.draw_filled_sphere(0.1, 20, 20)
        elif self.expression == 'sad':
            glRotatef(180, 1, 0, 0)
            glScalef(1, 0.5, 1)
            self.draw_filled_sphere(0.1, 20, 20)
        else:
            glScalef(1, 0.2, 1)
            self.draw_filled_sphere(0.1, 20, 20)
        glPopMatrix()

        glDisable(GL_LIGHTING)

    def draw(self):
        if not self.is_visible:  # Si no es visible, no dibujamos nada
            return
            
        glEnable(GL_DEPTH_TEST)
        glEnable(GL_CULL_FACE)
        glCullFace(GL_BACK)
        
        glPushMatrix()
        glTranslatef(*self.position)
        glTranslatef(0, self.jump_height, 0)
        glRotatef(self.rotation[0], 1, 0, 0)
        glRotatef(self.rotation[1], 0, 1, 0)
        glRotatef(self.rotation[2], 0, 0, 1)
        glScalef(*self.scale)

        if self.is_lying:
            glRotatef(90, 0, 0, 1)

        # [El resto del método draw se mantiene igual]
        # Cuerpo con sombreado
        glColor3fv(self.colors['body'])
        if self.is_crouching:
            self.draw_filled_cube(0.5)
            glTranslatef(0, -0.25, 0)
        else:
            glPushMatrix()
            glTranslatef(0, 0, 0)
            self.draw_filled_cube(0.5)
            glPopMatrix()

        # Cabeza con sombreado
        glColor3fv(self.colors['head'])
        glPushMatrix()
        if self.is_crouching:
            glTranslatef(0, 0.75, 0)
        else:
            glTranslatef(0, 1, 0)
        self.draw_filled_cube(0.3)
        self.draw_face()
        glPopMatrix()

        # Brazos con sombreado
        glColor3fv(self.colors['limbs'])
        # Brazo izquierdo
        glPushMatrix()
        glTranslatef(-0.7, 0, 0)
        glRotatef(self.left_arm_angle, 1, 0, 0)
        self.draw_filled_cube(0.2)
        glPopMatrix()

        # Brazo derecho
        glPushMatrix()
        glTranslatef(0.7, 0, 0)
        glRotatef(self.right_arm_angle, 1, 0, 0)
        self.draw_filled_cube(0.2)
        glPopMatrix()

        # Piernas con sombreado
        glColor3fv(self.colors['limbs'])
        leg_y = -1 if not self.is_crouching else -0.75

        # Pierna izquierda
        glPushMatrix()
        glTranslatef(-0.3, leg_y, 0)
        glRotatef(self.left_leg_angle, 1, 0, 0)
        self.draw_filled_cube(0.2)
        glPopMatrix()

        # Pierna derecha
        glPushMatrix()
        glTranslatef(0.3, leg_y, 0)
        if self.kick_angle > 0:
            glRotatef(-self.kick_angle, 1, 0, 0)
            self.kick_angle = max(0, self.kick_angle - 5)
        else:
            glRotatef(self.right_leg_angle, 1, 0, 0)
        self.draw_filled_cube(0.2)
        glPopMatrix()

        glPopMatrix()
        glDisable(GL_DEPTH_TEST)
        glDisable(GL_CULL_FACE)

    def walk(self):
        if not self.is_visible:  # Si no es visible, no actualizamos la animación
            return
        self.walk_cycle += 0.1
        if self.walk_cycle > math.pi * 2:
            self.walk_cycle = 0
        self.left_leg_angle = math.sin(self.walk_cycle) * 30
        self.right_leg_angle = math.sin(self.walk_cycle + math.pi) * 30
        self.left_arm_angle = math.sin(self.walk_cycle + math.pi) * 30
        self.right_arm_angle = math.sin(self.walk_cycle) * 30

    def jump(self):
        if not self.is_visible:  # Si no es visible, no actualizamos la animación
            return
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
        if not self.is_visible:  # Si no es visible, no actualizamos el estado
            return
        self.is_crouching = not self.is_crouching

    def lie_down(self):
        if not self.is_visible:  # Si no es visible, no actualizamos el estado
            return
        self.is_lying = not self.is_lying

    def kick(self):
        if not self.is_visible:  # Si no es visible, no actualizamos el estado
            return
        self.kick_angle = 45
    
    def reset(self):
        """Restaura todos los valores del enemigo a su estado inicial"""
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
        self.is_visible = True  # Restauramos la visibilidad

    def set_expression(self, expression):
        if not self.is_visible:  # Si no es visible, no actualizamos la expresión
            return
        self.expression = expression

    def remove(self):
        """Remueve el personaje de la pantalla haciéndolo invisible"""
        self.is_visible = False
        # Opcionalmente, podemos mover el personaje fuera de la vista
        self.position = [0.0, 0.0, 0.0]
        self.rotation = [0.0, 0.0, 0.0]
        
        

# Crear instancia del personaje
create_enemy = Enemy()