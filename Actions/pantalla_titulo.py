#Pantalla_titulo.py
import pygame
import sys
from . import sonidos as son

# Clase Button
class Button():
    def __init__(self, image, pos, text_input, font, base_color, hovering_color):
        self.image = image
        self.x_pos = pos[0]
        self.y_pos = pos[1]
        self.font = font
        self.base_color, self.hovering_color = base_color, hovering_color
        self.text_input = text_input
        self.text = self.font.render(self.text_input, True, self.base_color)
        if self.image is None:
            self.image = self.text
        self.rect = self.image.get_rect(center=(self.x_pos, self.y_pos))
        self.text_rect = self.text.get_rect(center=(self.x_pos, self.y_pos))

    def update(self, screen):
        if self.image is not None:
            screen.blit(self.image, self.rect)
        screen.blit(self.text, self.text_rect)

    def checkForInput(self, position):
        if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
            return True
        return False

    def changeColor(self, position):
        if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
            self.text = self.font.render(self.text_input, True, self.hovering_color)
        else:
            self.text = self.font.render(self.text_input, True, self.base_color)


# Clase PantallaTitulo con funcionalidad de Menú Principal
class PantallaTitulo:
    def __init__(self):
        pygame.init()

        # Configuración de la ventana
        self.ANCHO = 800
        self.ALTO = 600
        self.pantalla = pygame.display.set_mode((self.ANCHO, self.ALTO))
        pygame.display.set_caption("Bienvenido")  # Cambia esto por el nombre de tu juego
        self.fondo = pygame.image.load("welcome.jpg").convert()
        self.fondo = pygame.transform.scale(self.fondo, (self.ANCHO, self.ALTO))

        # Colores
        self.BLANCO = (255, 255, 255)

        # Fuentes
        self.fuente_titulo = pygame.font.Font(None, 64)
        self.fuente_mensaje = pygame.font.Font(None, 36)

        # Textos
        self.texto_titulo = "Aventura del Conocimiento"
        self.texto_mensaje = ""
        
        son.play_music("Sounds\principal0.mp3")

        # Botones del menú
        self.BTN_PLAY = Button(None, (self.ANCHO / 2, 300), "PLAY", self.fuente_titulo, (255, 255, 255), (0, 255, 0))
        self.BTN_OPTIONS = Button(None, (self.ANCHO / 2, 350), "", self.fuente_titulo, (255, 255, 255), (0, 255, 0))
        self.BTN_QUIT = Button(None, (self.ANCHO / 2, 400), "SALIR", self.fuente_titulo, (255, 255, 255), (0, 255, 0))

    def dibujar(self):
        # Dibujar el fondo
        self.pantalla.blit(self.fondo, (0, 0))
        
        # Renderiza el título
        titulo_superficie = self.fuente_titulo.render(self.texto_titulo, True, self.BLANCO)
        titulo_rect = titulo_superficie.get_rect(center=(self.ANCHO/2, self.ALTO/3))
        self.pantalla.blit(titulo_superficie, titulo_rect)
        
        mensaje_superficie = self.fuente_mensaje.render(self.texto_mensaje, True, self.BLANCO)
        mensaje_rect = mensaje_superficie.get_rect(center=(self.ANCHO/2, self.ALTO/2))
        self.pantalla.blit(mensaje_superficie, mensaje_rect)

        # Dibujar botones
        mouse_pos = pygame.mouse.get_pos()
        self.BTN_PLAY.changeColor(mouse_pos)
        self.BTN_PLAY.update(self.pantalla)

        self.BTN_OPTIONS.changeColor(mouse_pos)
        self.BTN_OPTIONS.update(self.pantalla)

        self.BTN_QUIT.changeColor(mouse_pos)
        self.BTN_QUIT.update(self.pantalla)

    def ejecutar(self):
        while True:
            self.dibujar()
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.BTN_PLAY.checkForInput(pygame.mouse.get_pos()):
                        return "play"  # Cambia a la siguiente pantalla de juego
                    elif self.BTN_OPTIONS.checkForInput(pygame.mouse.get_pos()):
                        return "options"  # Cambia a la pantalla de opciones
                    elif self.BTN_QUIT.checkForInput(pygame.mouse.get_pos()):
                        pygame.quit()
                        sys.exit()
            
            pygame.display.flip()
