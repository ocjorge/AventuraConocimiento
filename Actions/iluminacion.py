#Iluminación
from OpenGL.GLU import *
from OpenGL.GL import *
from OpenGL.GLUT import *

def phong(R, G, B):
    """
    Implementa el modelo de iluminación Phong, que calcula la iluminación por píxel
    proporcionando los reflejos más realistas de los tres modelos.
    R, G, B: Componentes de color en formato RGB (0.0 a 1.0)
    """
    glEnable(GL_LIGHTING) # Activa el sistema de iluminación de OpenGL
    glEnable(GL_LIGHT0)   # Activa la primera fuente de luz (luz 0)
    glEnable(GL_DEPTH_TEST) # Activa el test de profundidad para renderizado 3D correcto

    # Define las propiedades de la fuente de luz principal
    posicion_luz = (150.0, 250.0, -250.0, 1.0)  # (x, y, z, w) donde w=1.0 indica posición fija
    luz_ambiental = (0.1, 0.1, 0.1, 1.0)        # Luz base que afecta a toda la escena
    luz_difusa = (R, G, B, 1.0)                 # Color principal de la luz
    luz_especular = (1.0, 1.0, 1.0, 1.0)        # Color de los brillos especulares
    glLightfv(GL_LIGHT0, GL_POSITION, posicion_luz)
    glLightfv(GL_LIGHT0, GL_AMBIENT, luz_ambiental) 
    glLightfv(GL_LIGHT0, GL_DIFFUSE, luz_difusa)
    glLightfv(GL_LIGHT0, GL_SPECULAR, luz_especular)

    # Define las propiedades del material del objeto
    material_ambiente = (0.2, 0.2, 0.2, 1.0)     # Cómo el material refleja la luz ambiental
    material_difuso = (R, G, B, 1.0)             # Color base del material
    material_especular = (1.0, 1.0, 1.0, 1.0)    # Color de los reflejos del material
    brillo_especular = 50.0                      # Intensidad del brillo especular (0-128)
    glMaterialfv(GL_FRONT, GL_AMBIENT, material_ambiente)
    glMaterialfv(GL_FRONT, GL_DIFFUSE, material_difuso)
    glMaterialfv(GL_FRONT, GL_SPECULAR, material_especular)
    glMaterialfv(GL_FRONT, GL_SHININESS, brillo_especular)

    # Configuración específica del modelo Phong
    glEnable(GL_COLOR_MATERIAL)
    glColorMaterial(GL_FRONT, GL_AMBIENT_AND_DIFFUSE)

    # Asegura que todas las características de iluminación estén activas
    glEnable(GL_LIGHTING)
    glEnable(GL_LIGHT0)
    glEnable(GL_DEPTH_TEST)

def gouraud(R, G, B):
    """
    Implementa el modelo de iluminación Gouraud, que calcula la iluminación en los vértices
    y la interpola a través de las caras. Más rápido que Phong pero menos preciso.
    R, G, B: Componentes de color en formato RGB (0.0 a 1.0)
    """
    glEnable(GL_LIGHTING)   # Activa el sistema de iluminación
    glEnable(GL_LIGHT0)     # Activa la primera fuente de luz
    glEnable(GL_DEPTH_TEST) # Activa el test de profundidad

    # Configuración de la fuente de luz principal
    posicion_luz = (150.0, 250.0, -250.0, 1.0)   # Posición de la luz en el espacio 3D
    luz_ambiental = (0.1, 0.1, 0.1, 1.0)         # Iluminación ambiental mínima
    luz_difusa = (R, G, B, 1.0)                  # Color e intensidad de la luz
    luz_especular = (1.0, 1.0, 1.0, 1.0)         # Color del componente especular
    glLightfv(GL_LIGHT0, GL_POSITION, posicion_luz)
    glLightfv(GL_LIGHT0, GL_AMBIENT, luz_ambiental) 
    glLightfv(GL_LIGHT0, GL_DIFFUSE, luz_difusa)
    glLightfv(GL_LIGHT0, GL_SPECULAR, luz_especular)

    # Activa el modelo de sombreado Gouraud
    glShadeModel(GL_SMOOTH) # Interpolación suave entre vértices

    # Propiedades del material del objeto
    material_ambiente = (0.2, 0.2, 0.2, 1.0)      # Reflexión ambiental del material
    material_difuso = (R, G, B, 1.0)              # Color principal del material
    material_especular = (1.0, 1.0, 1.0, 1.0)     # Reflexión especular del material
    brillo_especular = 50.0                       # Factor de brillo
    glMaterialfv(GL_FRONT, GL_AMBIENT, material_ambiente)
    glMaterialfv(GL_FRONT, GL_DIFFUSE, material_difuso)
    glMaterialfv(GL_FRONT, GL_SPECULAR, material_especular)
    glMaterialfv(GL_FRONT, GL_SHININESS, brillo_especular)

    # Asegura la activación de la iluminación
    glEnable(GL_LIGHTING)
    glEnable(GL_LIGHT0)
    glEnable(GL_DEPTH_TEST)

def interpolado(R, G, B):
    """
    Implementa el modelo de iluminación plana (flat shading), que calcula la iluminación
    una vez por cara. Es el más rápido pero el menos realista de los tres modelos.
    R, G, B: Componentes de color en formato RGB (0.0 a 1.0)
    """
    glEnable(GL_LIGHTING)   # Activa el sistema de iluminación
    glEnable(GL_LIGHT0)     # Activa la primera fuente de luz
    glEnable(GL_DEPTH_TEST) # Activa el test de profundidad

    # Configuración de la luz
    posicion_luz = (150.0, 250.0, -250.0, 1.0)    # Posición fija de la luz
    luz_ambiental = (0.1, 0.1, 0.1, 1.0)          # Componente ambiental baja
    luz_difusa = (R, G, B, 1.0)                   # Color difuso principal
    luz_especular = (1.0, 1.0, 1.0, 1.0)          # Componente especular blanca
    glLightfv(GL_LIGHT0, GL_POSITION, posicion_luz)
    glLightfv(GL_LIGHT0, GL_AMBIENT, luz_ambiental) 
    glLightfv(GL_LIGHT0, GL_DIFFUSE, luz_difusa)
    glLightfv(GL_LIGHT0, GL_SPECULAR, luz_especular)

    # Activa el sombreado plano (un solo color por cara)
    glShadeModel(GL_FLAT)  # Sin interpolación entre vértices

    # Definición del material
    material_ambiente = (0.2, 0.2, 0.2, 1.0)       # Componente ambiental del material
    material_difuso = (R, G, B, 1.0)               # Color base del material
    material_especular = (1.0, 1.0, 1.0, 1.0)      # Componente especular del material
    brillo_especular = 50.0                        # Exponente especular
    glMaterialfv(GL_FRONT, GL_AMBIENT, material_ambiente)
    glMaterialfv(GL_FRONT, GL_DIFFUSE, material_difuso)
    glMaterialfv(GL_FRONT, GL_SPECULAR, material_especular)
    glMaterialfv(GL_FRONT, GL_SHININESS, brillo_especular)

    # Asegura que la iluminación esté correctamente configurada
    glEnable(GL_LIGHTING)
    glEnable(GL_LIGHT0)
    glEnable(GL_DEPTH_TEST)