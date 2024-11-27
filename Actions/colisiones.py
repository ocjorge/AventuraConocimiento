import math

def rombo_collision(
        PosObj2_X,
        PosObj2_Y,
        PosObj2_Z,
        Obj2_width,
        Obj2_height,
        Obj2_depth,
        posXobj1,
        posYobj1,
        posZobj1,
        Obj1_height
):
    obj2_rombo = (
        (PosObj2_X - Obj2_width / 2, PosObj2_Y, PosObj2_Z),  # Vértice inferior izquierdo
        (PosObj2_X, PosObj2_Y, PosObj2_Z - Obj2_depth / 2),  # Vértice superior
        (PosObj2_X + Obj2_width / 2, PosObj2_Y, PosObj2_Z),  # Vértice inferior derecho
        (PosObj2_X, PosObj2_Y + Obj2_height / 2, PosObj2_Z)  # Vértice medio
    )

    obj1_rombo = (
        (posXobj1 - 0.5, posYobj1, posZobj1),                # Vértice inferior izquierdo
        (posXobj1, posYobj1, posZobj1 - 0.5),                # Vértice superior
        (posXobj1 + 0.5, posYobj1, posZobj1),                # Vértice inferior derecho
        (posXobj1, posYobj1 + Obj1_height, posZobj1)        # Vértice medio
    )

    # Comprobación de colisiones
    for p1 in obj1_rombo:
        for p2 in obj2_rombo:
            distance = math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2 + (p1[2] - p2[2]) ** 2)
            if distance < 1.0:  # Radio de colisión
                return True  # Hay colisión

    return False  # No hay colisión
def rombo_collision_dos(
        PosObj2_X,
        PosObj2_Y,
        PosObj2_Z,
        Obj2_width,
        Obj2_height,
        Obj2_depth,
        posXobj1,
        posYobj1,
        posZobj1,
        Obj1_height
):
    obj3_rombo = (
        (PosObj2_X - Obj2_width / 2, PosObj2_Y, PosObj2_Z),  # Vértice inferior izquierdo
        (PosObj2_X, PosObj2_Y, PosObj2_Z - Obj2_depth / 2),  # Vértice superior
        (PosObj2_X + Obj2_width / 2, PosObj2_Y, PosObj2_Z),  # Vértice inferior derecho
        (PosObj2_X, PosObj2_Y + Obj2_height / 2, PosObj2_Z)  # Vértice medio
    )

    obj4_rombo = (
        (posXobj1 - 0.5, posYobj1, posZobj1),                # Vértice inferior izquierdo
        (posXobj1, posYobj1, posZobj1 - 0.5),                # Vértice superior
        (posXobj1 + 0.5, posYobj1, posZobj1),                # Vértice inferior derecho
        (posXobj1, posYobj1 + Obj1_height, posZobj1)        # Vértice medio
    )

    # Comprobación de colisiones
    for p1 in obj3_rombo:
        for p2 in obj4_rombo:
            distance = math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2 + (p1[2] - p2[2]) ** 2)
            if distance < 1.0:  # Radio de colisión
                return True  # Hay colisión

    return False  # No hay colisión

def rombo_collision_tres(
        PosObj2_X,
        PosObj2_Y,
        PosObj2_Z,
        Obj2_width,
        Obj2_height,
        Obj2_depth,
        posXobj1,
        posYobj1,
        posZobj1,
        Obj1_height
):
    obj3_rombo = (
        (PosObj2_X - Obj2_width, PosObj2_Y, PosObj2_Z),  # Vértice inferior izquierdo
        (PosObj2_X, PosObj2_Y, PosObj2_Z - Obj2_depth),  # Vértice superior
        (PosObj2_X + Obj2_width, PosObj2_Y, PosObj2_Z),  # Vértice inferior derecho
        (PosObj2_X, PosObj2_Y + Obj2_height, PosObj2_Z)  # Vértice medio
    )

    obj4_rombo = (
        (posXobj1 - 0.5, posYobj1, posZobj1),                # Vértice inferior izquierdo
        (posXobj1, posYobj1, posZobj1 - 0.5),                # Vértice superior
        (posXobj1 + 0.5, posYobj1, posZobj1),                # Vértice inferior derecho
        (posXobj1, posYobj1 + Obj1_height, posZobj1)        # Vértice medio
    )

    # Comprobación de colisiones
    for p1 in obj3_rombo:
        for p2 in obj4_rombo:
            distance = math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2 + (p1[2] - p2[2]) ** 2)
            if distance < 1.0:  # Radio de colisión
                return True  # Hay colisión

    return False  # No hay colisión

def aabb_collision(x1, y1, z1, width1, height1, depth1, x2, y2, z2, width2, height2, depth2):
    # Verificar colisión en el eje X
    if x1 + width1 < x2 or x1 > x2 + width2:
        return False
    # Verificar colisión en el eje Y
    if y1 + height1 < y2 or y1 > y2 + height2:
        return False
    # Verificar colisión en el eje Z
    if z1 + depth1 < z2 or z1 > z2 + depth2:
        return False
    return True

def aabb_sphere_collision(
    box_x, box_y, box_z, box_width, box_height, box_depth,
    sphere_x, sphere_y, sphere_z, sphere_radius
):
    """Detecta colisiones entre una caja AABB y una esfera"""
    # Encuentra el punto más cercano de la caja a la esfera
    closest_x = max(box_x, min(sphere_x, box_x + box_width))
    closest_y = max(box_y, min(sphere_y, box_y + box_height))
    closest_z = max(box_z, min(sphere_z, box_z + box_depth))

    # Calcula la distancia entre el punto más cercano y el centro de la esfera
    distance = math.sqrt(
        (closest_x - sphere_x) ** 2 +
        (closest_y - sphere_y) ** 2 +
        (closest_z - sphere_z) ** 2
    )

    return distance < sphere_radius

def aabb_capsule_collision(
    box_x, box_y, box_z, box_width, box_height, box_depth,
    cap_x, cap_y, cap_z, cap_radius, cap_height
):
    """Detecta colisiones entre una caja AABB y una cápsula"""
    # Primero verificamos la colisión con el cilindro central
    if aabb_cylinder_collision(
        box_x, box_y, box_z, box_width, box_height, box_depth,
        cap_x, cap_y, cap_z, cap_radius, cap_height
    ):
        return True

    # Luego verificamos las semiesferas en los extremos
    if aabb_sphere_collision(
        box_x, box_y, box_z, box_width, box_height, box_depth,
        cap_x, cap_y, cap_z, cap_radius
    ):
        return True

    if aabb_sphere_collision(
        box_x, box_y, box_z, box_width, box_height, box_depth,
        cap_x, cap_y + cap_height, cap_z, cap_radius
    ):
        return True

    return False

def aabb_cylinder_collision(
    box_x, box_y, box_z, box_width, box_height, box_depth,
    cyl_x, cyl_y, cyl_z, cyl_radius, cyl_height
):
    """Detecta colisiones entre una caja AABB y un cilindro"""
    # Verificar primero si hay superposición en Y
    if box_y + box_height < cyl_y or box_y > cyl_y + cyl_height:
        return False

    # Encontrar el punto más cercano en el plano XZ
    closest_x = max(box_x, min(cyl_x, box_x + box_width))
    closest_z = max(box_z, min(cyl_z, box_z + box_depth))

    # Calcular distancia en el plano XZ
    distance_xz = math.sqrt(
        (closest_x - cyl_x) ** 2 +
        (closest_z - cyl_z) ** 2
    )

    return distance_xz < cyl_radius

def aabb_cone_collision(
    box_x, box_y, box_z, box_width, box_height, box_depth,
    cone_x, cone_y, cone_z, cone_radius, cone_height
):
    """Detecta colisiones entre una caja AABB y un cono"""
    # Verificar primero si hay superposición en Y
    if box_y + box_height < cone_y or box_y > cone_y + cone_height:
        return False

    # Calcular el radio del cono en la altura actual
    for y in range(int(box_y), int(box_y + box_height)):
        height_ratio = (cone_height - (y - cone_y)) / cone_height
        current_radius = cone_radius * height_ratio

        # Encontrar el punto más cercano en el plano XZ
        closest_x = max(box_x, min(cone_x, box_x + box_width))
        closest_z = max(box_z, min(cone_z, box_z + box_depth))

        # Calcular distancia en el plano XZ
        distance_xz = math.sqrt(
            (closest_x - cone_x) ** 2 +
            (closest_z - cone_z) ** 2
        )

        if distance_xz < current_radius:
            return True

    return False

def get_rotated_vertices(x, y, z, width, height, depth, angle):
    """
    Calcula los vértices de una caja rotada en el espacio 3D.

    Args:
        x, y, z: Coordenadas de la esquina inferior frontal izquierda
        width, height, depth: Dimensiones de la caja
        angle: Ángulo de rotación en radianes

    Returns:
        Lista de tuplas (x, y, z) representando los vértices
    """
    cos_a = math.cos(angle)
    sin_a = math.sin(angle)

    vertices = [
        # Cara frontal
        (x, y, z),
        (x + width * cos_a, y, z - width * sin_a),
        (x + width * cos_a, y + height, z - width * sin_a),
        (x, y + height, z),
        # Cara trasera
        (x + depth * sin_a, y, z + depth * cos_a),
        (x + width * cos_a + depth * sin_a, y, z - width * sin_a + depth * cos_a),
        (x + width * cos_a + depth * sin_a, y + height, z - width * sin_a + depth * cos_a),
        (x + depth * sin_a, y + height, z + depth * cos_a)
    ]
    return vertices

def point_in_rotated_box(point, box_vertices):
    """
    Verifica si un punto está dentro de una caja rotada.

    Args:
        point: Tupla (x, y, z) del punto a verificar
        box_vertices: Lista de vértices de la caja rotada

    Returns:
        bool: True si el punto está dentro de la caja
    """
    x, y, z = point
    # Verificamos si el punto está dentro del prisma formado por los vértices
    min_x = min(v[0] for v in box_vertices)
    max_x = max(v[0] for v in box_vertices)
    min_y = min(v[1] for v in box_vertices)
    max_y = max(v[1] for v in box_vertices)
    min_z = min(v[2] for v in box_vertices)
    max_z = max(v[2] for v in box_vertices)

    return (min_x <= x <= max_x and
            min_y <= y <= max_y and
            min_z <= z <= max_z)

def aabb_oriented_collision(
    box1_x, box1_y, box1_z, box1_width, box1_height, box1_depth, box1_rotation,
    box2_x, box2_y, box2_z, box2_width, box2_height, box2_depth, box2_rotation
):
    """
    Detecta colisiones entre dos cajas AABB con rotación.

    Args:
        box1_x, box1_y, box1_z: Posición de la primera caja
        box1_width, box1_height, box1_depth: Dimensiones de la primera caja
        box1_rotation: Rotación de la primera caja en grados
        box2_x, box2_y, box2_z: Posición de la segunda caja
        box2_width, box2_height, box2_depth: Dimensiones de la segunda caja
        box2_rotation: Rotación de la segunda caja en grados

    Returns:
        bool: True si hay colisión, False en caso contrario
    """
    # Convertir ángulos a radianes
    angle1 = math.radians(box1_rotation)
    angle2 = math.radians(box2_rotation)

    # Calcular los vértices de las cajas rotadas
    vertices1 = get_rotated_vertices(box1_x, box1_y, box1_z,
                                   box1_width, box1_height, box1_depth, angle1)
    vertices2 = get_rotated_vertices(box2_x, box2_y, box2_z,
                                   box2_width, box2_height, box2_depth, angle2)

    # Verificar colisión en ambas direcciones
    # Si cualquier vértice de la caja 1 está dentro de la caja 2
    for vertex in vertices1:
        if point_in_rotated_box(vertex, vertices2):
            return True

    # Si cualquier vértice de la caja 2 está dentro de la caja 1
    for vertex in vertices2:
        if point_in_rotated_box(vertex, vertices1):
            return True

    return False

def project_vertices(vertices, axis):
    """
    Proyecta todos los vértices sobre un eje y retorna el mínimo y máximo.
    """
    dots = [sum(v[i] * axis[i] for i in range(len(v))) for v in vertices]
    return min(dots), max(dots)

def get_axes(vertices):
    """
    Obtiene todos los ejes perpendiculares a cada lado del polígono.
    """
    axes = []
    for i in range(len(vertices)):
        # Obtener el vector del lado actual
        p1 = vertices[i]
        p2 = vertices[(i + 1) % len(vertices)]
        edge = (p2[0] - p1[0], p2[1] - p1[1], p2[2] - p1[2])

        # Generar ejes perpendiculares
        axis1 = (-edge[1], edge[0], 0)
        length = math.sqrt(sum(x * x for x in axis1))
        if length > 0:
            axis1 = tuple(x / length for x in axis1)
            axes.append(axis1)

        axis2 = (0, -edge[2], edge[1])
        length = math.sqrt(sum(x * x for x in axis2))
        if length > 0:
            axis2 = tuple(x / length for x in axis2)
            axes.append(axis2)

    return axes

def sat_collision(vertices1, vertices2):
    """
    Implementa el Teorema del Eje de Separación (SAT) para detectar colisiones entre dos polígonos convexos en 3D.

    Args:
        vertices1: Lista de tuplas (x, y, z) representando los vértices del primer polígono
        vertices2: Lista de tuplas (x, y, z) representando los vértices del segundo polígono

    Returns:
        bool: True si hay colisión, False si no hay colisión
    """
    # Obtener todos los ejes a comprobar
    axes = get_axes(vertices1) + get_axes(vertices2)

    # Comprobar cada eje
    for axis in axes:
        # Proyectar ambos polígonos sobre el eje
        proj1_min, proj1_max = project_vertices(vertices1, axis)
        proj2_min, proj2_max = project_vertices(vertices2, axis)

        # Verificar si hay separación
        if proj1_max < proj2_min or proj2_max < proj1_min:
            return False  # Se encontró un eje de separación, no hay colisión

    return True  # No se encontró eje de separación, hay colisión

def sat_collision_boxes(
    box1_x, box1_y, box1_z, box1_width, box1_height, box1_depth,
    box2_x, box2_y, box2_z, box2_width, box2_height, box2_depth
):
    """
    Implementa colisión SAT específicamente para cajas AABB.
    """
    # Definir vértices de la primera caja
    vertices1 = [
        (box1_x, box1_y, box1_z),
        (box1_x + box1_width, box1_y, box1_z),
        (box1_x + box1_width, box1_y + box1_height, box1_z),
        (box1_x, box1_y + box1_height, box1_z),
        (box1_x, box1_y, box1_z + box1_depth),
        (box1_x + box1_width, box1_y, box1_z + box1_depth),
        (box1_x + box1_width, box1_y + box1_height, box1_z + box1_depth),
        (box1_x, box1_y + box1_height, box1_z + box1_depth)
    ]

    # Definir vértices de la segunda caja
    vertices2 = [
        (box2_x, box2_y, box2_z),
        (box2_x + box2_width, box2_y, box2_z),
        (box2_x + box2_width, box2_y + box2_height, box2_z),
        (box2_x, box2_y + box2_height, box2_z),
        (box2_x, box2_y, box2_z + box2_depth),
        (box2_x + box2_width, box2_y, box2_z + box2_depth),
        (box2_x + box2_width, box2_y + box2_height, box2_z + box2_depth),
        (box2_x, box2_y + box2_height, box2_z + box2_depth)
    ]

    return sat_collision(vertices1, vertices2)

def get_rhombus_vertices(pos_x, pos_y, pos_z, width, height, depth):
    """
    Obtiene los vértices de un rombo en 3D.
    """
    return [
        (pos_x - width/2, pos_y, pos_z),           # Vértice inferior izquierdo
        (pos_x, pos_y, pos_z - depth/2),           # Vértice superior
        (pos_x + width/2, pos_y, pos_z),           # Vértice inferior derecho
        (pos_x, pos_y + height/2, pos_z),          # Vértice medio
        (pos_x, pos_y - height/2, pos_z),          # Vértice inferior
    ]

def rombo_collision_sat(
    PosObj2_X, PosObj2_Y, PosObj2_Z,
    Obj2_width, Obj2_height, Obj2_depth,
    posXobj1, posYobj1, posZobj1,
    Obj1_height
):
    """
    Función de colisión SAT para rombos que mantiene la misma interfaz que la original.
    """
    # Obtener vértices del primer rombo
    vertices1 = get_rhombus_vertices(
        PosObj2_X, PosObj2_Y, PosObj2_Z,
        Obj2_width, Obj2_height, Obj2_depth
    )

    # Obtener vértices del segundo rombo (usando dimensiones fijas como en el original)
    vertices2 = get_rhombus_vertices(
        posXobj1, posYobj1, posZobj1,
        1.0, Obj1_height, 1.0  # Ancho y profundidad fijos como en el original
    )

    # Realizar la detección de colisión SAT
    return sat_collision(vertices1, vertices2)
