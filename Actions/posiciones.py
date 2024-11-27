#posiciones.py
class GamePositions:
    def __init__(self):
        # Posiciones iniciales del objeto1 (personaje 1)
        self.PosX_objeto1 = 12
        self.PosY_objeto1 = 6
        self.PosZ_objeto1 = 4
        self.objeto1_height = 1
        self.objeto1_width = 1
        self.objeto1_depth = 1
        self.objeto1_size = 2

        # Posiciones iniciales del objeto11 (personaje 2)
        self.PosX_objeto11 = 6
        self.PosY_objeto11 = 6
        self.PosZ_objeto11 = 4
        self.objeto11_height = 1
        self.objeto11_width = 1
        self.objeto11_depth = 1
        self.objeto11_size = 2

        # Posiciones iniciales del objeto21 (personaje 3)
        self.PosX_objeto21 = 0
        self.PosY_objeto21 = 6
        self.PosZ_objeto21 = 4
        self.objeto21_height = 1
        self.objeto21_width = 1
        self.objeto21_depth = 1
        self.objeto21_size = 2

        self.PosX_objeto2 = 20
        self.PosY_objeto2 = 20
        self.PosZ_objeto2 = 20
        self.obj2_height = 1
        self.objeto2_width = 4
        self.objeto2_height = 4
        self.objeto2_depth = 4

        self.PosX_objeto3 = 21
        self.PosY_objeto3 = 21
        self.PosZ_objeto3 = 21
        self.obj3_height = 1
        self.objeto3_width = 1
        self.objeto3_height = 1
        self.objeto3_depth = 1
        self.objeto3_radius = 5
        self.objeto3_size = 2

        self.PosX_objeto4 = -20
        self.PosY_objeto4 = -20
        self.PosZ_objeto4 = -20
        self.obj4_height = 1
        self.objeto4_width = 1
        self.objeto4_height = 1
        self.objeto4_depth = 1
        self.objeto4_radius = 15
        self.objeto4_size = 3

        self.PosX_objeto5 = -21
        self.PosY_objeto5 = -21
        self.PosZ_objeto5 = -21
        self.objeto5_radius = 1
        self.objeto5_height = 3
        self.obj5_height = 3
        self.objeto5_depth = 1

        # Asignando valores al azar hasta el objeto 16
        self.PosX_objeto6 = 22
        self.PosY_objeto6 = 22
        self.PosZ_objeto6 = 22
        self.objeto6_width = 2
        self.objeto6_height = 5
        self.objeto6_depth = 3

        self.PosX_objeto7 = 23
        self.PosY_objeto7 = 23
        self.PosZ_objeto7 = 23
        self.objeto7_width = 3
        self.objeto7_height = 2
        self.objeto7_depth = 4
        self.objeto7_radius = 7
        self.objeto7_size = 3

        self.PosX_objeto8 = -22
        self.PosY_objeto8 = -22
        self.PosZ_objeto8 = -22
        self.objeto8_width = 1
        self.objeto8_height = 4
        self.objeto8_depth = 2
        self.objeto8_radius = 9
        self.objeto8_size = 5

        self.PosX_objeto9 = -23
        self.PosY_objeto9 = -23
        self.PosZ_objeto9 = -23
        self.objeto9_width = 2
        self.objeto9_height = 3
        self.objeto9_depth = 1
        self.objeto9_radius = 6
        self.objeto9_size = 2

        self.PosX_objeto10 = 24
        self.PosY_objeto10 = 24
        self.PosZ_objeto10 = 24
        self.objeto10_width = 5
        self.objeto10_height = 2
        self.objeto10_depth = 4
        self.objeto10_radius = 12
        self.objeto10_size = 4

        self.PosX_objeto11 = -23
        self.PosY_objeto11 = -23
        self.PosZ_objeto11 = -23
        self.objeto11_width = 3
        self.objeto11_height = 3
        self.objeto11_depth = 3

        self.PosX_objeto12 = -24
        self.PosY_objeto12 = -24
        self.PosZ_objeto12 = -24
        self.objeto12_width = 2
        self.objeto12_height = 1
        self.objeto12_depth = 5
        self.objeto12_radius = 8
        self.objeto12_size = 3

        self.PosX_objeto13 = 25
        self.PosY_objeto13 = 25
        self.PosZ_objeto13 = 25
        self.objeto13_width = 4
        self.objeto13_height = 2
        self.objeto13_depth = 2
        self.objeto13_radius = 10
        self.objeto13_size = 6

        self.PosX_objeto14 = 26
        self.PosY_objeto14 = 26
        self.PosZ_objeto14 = 26
        self.objeto14_width = 3
        self.objeto14_height = 4
        self.objeto14_depth = 1
        self.objeto14_radius = 11
        self.objeto14_size = 2

        self.PosX_objeto15 = -25
        self.PosY_objeto15 = -25
        self.PosZ_objeto15 = -25
        self.objeto15_width = 1
        self.objeto15_height = 3
        self.objeto15_depth = 4
        self.objeto15_radius = 14
        self.objeto15_size = 3

        self.PosX_objeto16 = -26
        self.PosY_objeto16 = -26
        self.PosZ_objeto16 = -26
        self.objeto16_width = 2
        self.objeto16_height = 5
        self.objeto16_depth = 3
        self.objeto16_radius = 13
        self.objeto16_size = 4

        self.PosX_objeto17 = -20
        self.PosY_objeto17 = 20
        self.PosZ_objeto17 = -20
        self.objeto17_width = 4
        self.objeto17_height = 3
        self.objeto17_depth = 2
        self.objeto17_radius = 10
        self.objeto17_size = 3

        self.PosX_objeto18 = 20
        self.PosY_objeto18 = -20
        self.PosZ_objeto18 = 20
        self.objeto18_width = 2
        self.objeto18_height = 5
        self.objeto18_depth = 3
        self.objeto18_radius = 12
        self.objeto18_size = 4

        self.PosX_objeto19 = -25
        self.PosY_objeto19 = 25
        self.PosZ_objeto19 = -25
        self.objeto19_width = 3
        self.objeto19_height = 2
        self.objeto19_depth = 1
        self.objeto19_radius = 8
        self.objeto19_size = 2

        self.PosX_objeto20 = 25
        self.PosY_objeto20 = -25
        self.PosZ_objeto20 = 25
        self.objeto20_width = 2
        self.objeto20_height = 4
        self.objeto20_depth = 3
        self.objeto20_radius = 6
        self.objeto20_size = 3

        self.PosX_objeto21 = 23
        self.PosY_objeto21 = -23
        self.PosZ_objeto21 = 23
        self.objeto21_width = 4
        self.objeto21_height = 1
        self.objeto21_depth = 2
        self.objeto21_radius = 7
        self.objeto21_size = 5

        self.PosX_objeto22 = -23
        self.PosY_objeto22 = 23
        self.PosZ_objeto22 = -23
        self.objeto22_width = 1
        self.objeto22_height = 3
        self.objeto22_depth = 4
        self.objeto22_radius = 9
        self.objeto22_size = 2

        self.PosX_objeto23 = -22
        self.PosY_objeto23 = -22
        self.PosZ_objeto23 = 22
        self.objeto23_width = 3
        self.objeto23_height = 4
        self.objeto23_depth = 2
        self.objeto23_radius = 11
        self.objeto23_size = 3

        self.PosX_objeto24 = 22
        self.PosY_objeto24 = 22
        self.PosZ_objeto24 = -22
        self.objeto24_width = 2
        self.objeto24_height = 3
        self.objeto24_depth = 3
        self.objeto24_radius = 12
        self.objeto24_size = 4

        self.PosX_objeto25 = -21
        self.PosY_objeto25 = 22
        self.PosZ_objeto25 = 21
        self.objeto25_width = 4
        self.objeto25_height = 2
        self.objeto25_depth = 4
        self.objeto25_radius = 10
        self.objeto25_size = 5

        self.PosX_objeto26 = -21
        self.PosY_objeto26 = -23
        self.PosZ_objeto26 = 24
        self.objeto26_width = 3
        self.objeto26_height = 5
        self.objeto26_depth = 2
        self.objeto26_radius = 13
        self.objeto26_size = 3



    def get_character_position(self, character_number):
        if character_number == 1:
            return (self.PosX_objeto1, self.PosY_objeto1, self.PosZ_objeto1)
        elif character_number == 2:
            return (self.PosX_objeto11, self.PosY_objeto11, self.PosZ_objeto11)
        elif character_number == 3:
            return (self.PosX_objeto21, self.PosY_objeto21, self.PosZ_objeto21)
        return (0, 0, 0)

    def get_character_size(self, character_number):
        if character_number == 1:
            return {
                'width': self.objeto1_width,
                'height': self.objeto1_height,
                'depth': self.objeto1_depth
            }
        elif character_number == 2:
            return {
                'width': self.objeto11_width,
                'height': self.objeto11_height,
                'depth': self.objeto11_depth
            }
        elif character_number == 3:
            return {
                'width': self.objeto21_width,
                'height': self.objeto21_height,
                'depth': self.objeto21_depth
            }
        return {'width': 1, 'height': 1, 'depth': 1}

    def update_position(self, character_number, x=None, y=None, z=None):
        if character_number == 1:
            if x is not None: self.PosX_objeto1 = x
            if y is not None: self.PosY_objeto1 = y
            if z is not None: self.PosZ_objeto1 = z
        elif character_number == 2:
            if x is not None: self.PosX_objeto11 = x
            if y is not None: self.PosY_objeto11 = y
            if z is not None: self.PosZ_objeto11 = z
        elif character_number == 3:
            if x is not None: self.PosX_objeto21 = x
            if y is not None: self.PosY_objeto21 = y
            if z is not None: self.PosZ_objeto21 = z

   

# Crear una instancia global
game_positions = GamePositions()
