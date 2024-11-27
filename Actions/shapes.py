# shapes.py
import math
from OpenGL.GL import *

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