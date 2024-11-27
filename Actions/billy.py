#billy.py
import pygame
import math
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

# Colores
WHITE = (1, 1, 1)
BLACK = (0, 0, 0)
ORANGE = (1.0, 0.5, 0.0)
BROWN = (0.6, 0.3, 0)
RED = (1.0, 0.0, 0.0)

def setup_lighting():
    """Configura la iluminación global"""
    glEnable(GL_LIGHTING)
    glEnable(GL_LIGHT0)
    glEnable(GL_DEPTH_TEST)
    glEnable(GL_COLOR_MATERIAL)
    glColorMaterial(GL_FRONT_AND_BACK, GL_AMBIENT_AND_DIFFUSE)

    light_position = [0.0, 10.0, 10.0, 1.0]
    glLightfv(GL_LIGHT0, GL_POSITION, light_position)

    white_light = [1.0, 1.0, 1.0, 1.0]
    lmodel_ambient = [0.4, 0.4, 0.4, 1.0]
    glLightfv(GL_LIGHT0, GL_DIFFUSE, white_light)
    glLightfv(GL_LIGHT0, GL_SPECULAR, white_light)
    glLightModelfv(GL_LIGHT_MODEL_AMBIENT, lmodel_ambient)

    glMaterialfv(GL_FRONT, GL_SPECULAR, [0.3, 0.3, 0.3, 1.0])
    glMaterialf(GL_FRONT, GL_SHININESS, 50.0)

def set_material_color(color):
    """Establece el color del material con propiedades de iluminación"""
    if not isinstance(color, tuple) or len(color) != 3:
        raise ValueError("Color must be a tuple of 3 float values")
    glMaterialfv(GL_FRONT, GL_AMBIENT_AND_DIFFUSE, color + (1.0,))


class Snowman:
    def __init__(self):
        self.position = [0.0, 0.0, 0.0]
        self.rotation = [0.0, 0.0, 0.0]
        self.scale = [1.0, 1.0, 1.0]
        self.expression = 'neutral'
        self.left_arm_angle = 0.0
        self.right_arm_angle = 0.0
        self.walk_cycle = 0.0
        self.jump_cycle = 0.0
        self.jump_height = 0.0
        self.is_jumping = False
        self.is_crouching = False
        self.is_lying = False
        self.kick_angle = 0.0
        self.base_scale = 5.0
        self.visible = True  # Agregamos esta línea
        self.gl_resources = []  # Y esta línea
        self.collision_info = {
            'x': 0.0,
            'y': 0.0,
            'z': 0.0,
            'width': float(self.base_scale),
            'height': float(self.base_scale * 2),
            'depth': float(self.base_scale)
        }


    def draw_sphere(self, radius: float, slices: int, stacks: int) -> None:
        """Dibuja una esfera con los parámetros especificados"""
        if not isinstance(radius, (int, float)) or radius <= 0:
            raise ValueError("Radius must be a positive number")
        if not isinstance(slices, int) or slices < 3:
            raise ValueError("Slices must be an integer >= 3")
        if not isinstance(stacks, int) or stacks < 2:
            raise ValueError("Stacks must be an integer >= 2")

        for i in range(stacks):
            lat0 = math.pi * (-0.5 + float(i) / stacks)
            z0 = math.sin(lat0)
            zr0 = math.cos(lat0)

            lat1 = math.pi * (-0.5 + float(i + 1) / stacks)
            z1 = math.sin(lat1)
            zr1 = math.cos(lat1)

            glBegin(GL_QUAD_STRIP)
            for j in range(slices + 1):
                lng = 2 * math.pi * float(j - 1) / slices
                x = math.cos(lng)
                y = math.sin(lng)

                glNormal3f(x * zr0, y * zr0, z0)
                glVertex3f(x * zr0 * radius, y * zr0 * radius, z0 * radius)
                
                glNormal3f(x * zr1, y * zr1, z1)
                glVertex3f(x * zr1 * radius, y * zr1 * radius, z1 * radius)
            glEnd()

    @staticmethod

    def draw_cylinder(radius: float, height: float, slices: int) -> None:
        """Dibuja un cilindro con los parámetros especificados"""
        if not isinstance(radius, (int, float)) or radius <= 0:
            raise ValueError("Radius must be a positive number")
        if not isinstance(height, (int, float)) or height <= 0:
            raise ValueError("Height must be a positive number")
        if not isinstance(slices, int) or slices < 3:
            raise ValueError("Slices must be an integer >= 3")

        # Superficie lateral
        glBegin(GL_QUAD_STRIP)
        for i in range(slices + 1):
            angle = 2.0 * math.pi * float(i) / float(slices)
            x = math.cos(angle)
            y = math.sin(angle)
            
            glNormal3f(x, 0.0, y)
            glVertex3f(x * radius, 0.0, y * radius)
            glVertex3f(x * radius, height, y * radius)
        glEnd()


        # Tapas
        for h in [0.0, height]:
            glBegin(GL_POLYGON)
            glNormal3f(0.0, -1.0 if h == 0.0 else 1.0, 0.0)
            for i in range(slices):
                angle = 2.0 * math.pi * float(i) / float(slices)
                x = radius * math.cos(angle)
                y = radius * math.sin(angle)
                glVertex3f(x, h, y)
            glEnd()

    def update_collision_info(self):
        """Actualiza la información de colisión"""
        self.collision_info.update({
            'x': float(self.position[0]),
            'y': float(self.position[1]),
            'z': float(self.position[2])
        })
    def set_expression(self, expression: str) -> None:
        """Establece la expresión del muñeco de nieve"""
        valid_expressions = {'neutral', 'smile', 'frown', 'wink', 'fear', 'angry', 'doubt', 'admiration'}
        if expression not in valid_expressions:
            raise ValueError(f"Invalid expression. Must be one of: {valid_expressions}")
        self.expression = expression
 
    def reset(self):
        self.__init__()

    def translate(self, x, y, z):
        """Traslada el muñeco de nieve"""
        self.position[0] += x
        self.position[1] += y
        self.position[2] += z
        self.update_collision_info()

    def rotate(self, angle, x, y, z):
        """Rota el muñeco de nieve"""
        self.rotation[0] += float(angle * x)
        self.rotation[1] += float(angle * y)
        self.rotation[2] += float(angle * z)

    def reset(self):
        """Reinicia todos los valores a su estado original"""
        self.__init__()
        self.position = [0.0, 0.0, 0.0]
        self.rotation = [0.0, 0.0, 0.0]
        self.head_rotation = [0.0, 0.0, 0.0]
        self.scale = [1.0, 1.0, 1.0]
        self.expression = 'neutral'
        self.left_arm_angle = 0.0
        self.right_arm_angle = 0.0
        self.walk_cycle = 0.0
        self.jump_cycle = 0.0
        self.jump_height = 0.0
        self.is_jumping = False
        self.is_crouching = False
        self.is_lying = False
        self.kick_angle = 0.0
        self.update_collision_info()

    def walk(self):
        self.walk_cycle += 0.1
        if self.walk_cycle > math.pi * 2:
            self.walk_cycle = 0
        self.left_arm_angle = math.sin(self.walk_cycle) * 30
        self.right_arm_angle = math.sin(self.walk_cycle + math.pi) * 30

    def jump(self):
        if not self.is_jumping:
            self.is_jumping = True
            self.jump_cycle = 0
        if self.is_jumping:
            self.jump_height = math.sin(self.jump_cycle) * self.base_scale * 0.2
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

    def wave(self):
        self.right_arm_angle = math.sin(pygame.time.get_ticks() * 0.01) * 45


    def draw_face(self):
        scale_factor = self.base_scale * 0.25  # Factor de escala para la cara
        # Nariz (zanahoria) - Aumentar el tamaño
        glColor3f(*ORANGE)
        glPushMatrix()
        glTranslatef(0, 0, 0.35 * self.base_scale)
        glRotatef(90, 1, 0, 0)
        self.draw_cylinder(0.1 * scale_factor, 0.3 * scale_factor, 8)  # Aumentado el tamaño
        glPopMatrix()

        # Ojos
        glColor3f(*BLACK)
        # Ojo izquierdo
        glPushMatrix()
        glTranslatef(-0.1 * scale_factor, 0.1 * scale_factor, 0.35 * scale_factor)
        self.draw_sphere(0.06 * scale_factor, 10, 10)  # Aumentado el tamaño
        glPopMatrix()

        # Ojo derecho
        glPushMatrix()
        glTranslatef(0.1 * scale_factor, 0.1 * scale_factor, 0.35 * scale_factor)
        self.draw_sphere(0.06 * scale_factor, 10, 10)  # Aumentado el tamaño
        glPopMatrix()

        # Boca - Aumentar la visibilidad
        glColor3f(*BLACK)
        glPushMatrix()
        glTranslatef(0, -0.1 * scale_factor, 0.35 * scale_factor)
        self.draw_sphere(0.12 * scale_factor, 10, 10)  # Aumentado el tamaño
        glPopMatrix()
        
        if self.expression == 'smile':
            glScalef(1, 0.5, 1)
            self.draw_sphere(0.1 * scale_factor, 10, 10)
        elif self.expression == 'frown':
            glRotatef(180, 1, 0, 0)
            glScalef(1, 0.5, 1)
            self.draw_sphere(0.1 * scale_factor, 10, 10)
        elif self.expression == 'fear':
            glScalef(0.5, 1, 1)
            self.draw_sphere(0.1 * scale_factor, 10, 10)
        elif self.expression == 'angry':
            glScalef(1, 0.3, 1)
            self.draw_sphere(0.08 * scale_factor, 10, 10)
        else:
            glScalef(1, 0.2, 1)
            self.draw_sphere(0.1 * scale_factor, 10, 10)
        glPopMatrix()

    def draw_arm(self, is_right=True, angle=0):
        arm_length = self.base_scale * 0.6  # Aumentar la longitud del brazo
        arm_radius = self.base_scale * 0.05   # Aumentar el grosor del brazo
        

        glPushMatrix()
        if is_right:
            glRotatef(angle, 1, 0, 0)
            glTranslatef(arm_length / 2, -arm_length / 2, 0)  # Ajuste para mejor posición
        else:
            glRotatef(-angle, 1, 0, 0)
            glTranslatef(-arm_length / 2, -arm_length / 2, 0) 
        # Tronco principal
        glColor3f(*BROWN)
        self.draw_cylinder(arm_radius, arm_length, 8)
        
        # Ramitas en la punta
        for angle_offset in [-30, -60]:
            glPushMatrix()
            glTranslatef(0, arm_length, 0)
            glRotatef(angle_offset, 0, 0, 1)
            self.draw_cylinder(arm_radius * 0.7, arm_length * 0.3, 8)
            glPopMatrix()
        
        glPopMatrix()

    def draw_hat(self):
        # Dimensiones del sombrero ajustadas
        hat_base_radius = self.base_scale * 0.25  # Base del sombrero
        hat_top_radius = self.base_scale * 0.2     # Ajustado para mejor proporción
        hat_height = self.base_scale * 0.3          # Altura del sombrero
        brim_radius = self.base_scale * 0.35        # Ajustado el ala
        brim_height = self.base_scale * 0.05        # Altura del ala
        # Color del sombrero más negro para contraste
        glColor3f(0, 0, 0)

        # Ala del sombrero - Ajustar la posición para que esté erguido
        glPushMatrix()
        glTranslatef(0, 0, 0) 
        #glTranslatef(0, -brim_height / 2 + hat_height / 2, 0)
        glRotatef(1,180 ,0 ,0 )
       
        self.draw_cylinder(brim_radius , brim_height ,32)
        
        # Copa del sombrero - Ajustar la posición y rotación para que esté erguido
        glPushMatrix()
        
        glTranslatef(0, hat_height / 2, 0)
    
        # Rotación corregida para que esté erguido 
        self.draw_cylinder(hat_top_radius , hat_height ,32)
        glPopMatrix()

        # Banda decorativa del sombrero 
        glColor3f(0.7 ,0.1 , 0.1) 
        glPushMatrix() 
        glTranslatef(0 ,hat_height* .1 , -brim_height/2 ) 
        self.draw_cylinder(hat_top_radius + .01 ,hat_height* .1 ,32) 
        glPopMatrix() 
        
    def draw_buttons(self):
        button_radius = self.base_scale * 0.05
        glColor3f(*BLACK)
        
        # Dibuja 3 botones en el torso
        for i in range(3):
            glPushMatrix()
            glTranslatef(0, (i - 1) * button_radius * 4, self.base_scale * 0.35)
            self.draw_sphere(button_radius, 10, 10)
            glPopMatrix()

    def remove(self):
        """Oculta el muñeco de nieve de la pantalla"""
        self.visible = False
        # Reiniciar la posición y otros valores por si se necesita volver a mostrar
        self.position = [0.0, 0.0, 0.0]
        self.rotation = [0.0, 0.0, 0.0]
        self.scale = [1.0, 1.0, 1.0]
        self.update_collision_info()
    
    def show(self):
        """Vuelve a mostrar el muñeco de nieve en la pantalla"""
        self.visible = True

    def draw(self):
        
        if not self.visible:
            return  # No dibuja nada si no es visible
        
        setup_lighting()  # Configurar la iluminación antes de dibujar
        glPushMatrix()
        
        # Aplicar transformaciones globales
        glTranslatef(*self.position)
        glTranslatef(0, self.jump_height, 0)
        
        if self.is_lying:
            glRotatef(90, 0, 0, 1)
        
        glRotatef(self.rotation[0], 1, 0, 0)
        glRotatef(self.rotation[1], 0, 1, 0)
        glRotatef(self.rotation[2], 0, 0, 1)
        
        scale_factor = 1.0 if not self.is_crouching else 0.7
        glScalef(scale_factor, scale_factor, scale_factor)

        # Base (más grande)
        glColor3f(*WHITE)
        glPushMatrix()
        glTranslatef(0, -0.5 * self.base_scale, 0)
        self.draw_sphere(0.5 * self.base_scale,20, 20)
        glPopMatrix()

        # Torso (tamaño medio)
        glColor3f(*WHITE)
        glPushMatrix()
        glTranslatef(0, 0.2 * self.base_scale, 0)
        self.draw_sphere(0.35 * self.base_scale, 20, 20)
        self.draw_buttons()
        glPopMatrix()

        set_material_color(BLACK)
        for i in range(3):
            glPushMatrix()
            glTranslatef(0, (i - 1) * self.base_scale * 0.1, self.base_scale * 0.35)
            self.draw_sphere(0.05 * self.base_scale, 10, 10)
            glPopMatrix()
        glPopMatrix()
       

        # Cabeza
        glColor3f(*WHITE)
        set_material_color(WHITE)
        glPushMatrix()
        glTranslatef(0, 0.8 * self.base_scale, 0)
        self.draw_sphere(0.25 * self.base_scale, 20, 20)

        # Nariz (zanahoria)
        glColor3f(*ORANGE)
        set_material_color(ORANGE)
        glPushMatrix()
        glTranslatef(0, 0, 0.25 * self.base_scale)
        glRotatef(90, 1, 0, 0)
        self.draw_cylinder(0.05 * self.base_scale, 0.2 * self.base_scale, 8)
        glPopMatrix()

         # Ojos
        set_material_color(BLACK)
        glPushMatrix()
        glTranslatef(-0.1 * self.base_scale, 0.1 * self.base_scale, 0.2 * self.base_scale)
        self.draw_sphere(0.03 * self.base_scale, 10, 10)
        glPopMatrix()

        glPushMatrix()
        glTranslatef(0.1 * self.base_scale, 0.1 * self.base_scale, 0.2 * self.base_scale)
        self.draw_sphere(0.03 * self.base_scale, 10, 10)
        glPopMatrix()
        
        # Sombrero
        glColor3f(*BLACK)
        glPushMatrix()
        glTranslatef(0, 0.3 * self.base_scale, 0)  # Ajustado para que se asiente mejor en la cabeza
        self.draw_hat()
        glPopMatrix()
        
        glPopMatrix()

# Brazos
        set_material_color(BROWN)
        glPushMatrix()
        glTranslatef(0.4 * self.base_scale, 0.2 * self.base_scale, 0)
        glRotatef(self.right_arm_angle, 1, 0, 0)
        self.draw_cylinder(0.05 * self.base_scale, 0.4 * self.base_scale, 8)
        glPopMatrix()

        glPushMatrix()
        glTranslatef(-0.4 * self.base_scale, 0.2 * self.base_scale, 0)
        glRotatef(self.left_arm_angle, 1, 0, 0)
        self.draw_cylinder(0.05 * self.base_scale, 0.4 * self.base_scale, 8)
        glPopMatrix()

        glPopMatrix()

# Ejemplo de uso:
# snowman = Snowman()
# En el bucle principal:
# snowman.walk()  # Para hacer que camine
# snowman.jump()  # Para hacerlo saltar
# snowman.crouch()  # Para agacharse
# snowman.lie_down()  # Para acostarse
# snowman.kick()  # Para patear
# snowman.wave()  # Para saludar
# snowman.set_expression('smile')  # Para cambiar la expresión
# snowman.draw()  # Para dibujarlo