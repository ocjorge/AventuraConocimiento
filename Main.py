#main.py
import pygame
import numpy as np
import math
import os
from OpenGL.GLU import *
from OpenGL.GL import *
from OpenGL.GLUT import *
from pygame.locals import *
from PIL import *
from Actions import escenarios as esv
from Actions import iluminacion as lc
from Actions import objetos as obj
from Actions import sonidos as son
from Actions import textos as txt
from Actions.posiciones import GamePositions
from Actions import colisiones as coli
from Actions import billy as billy
from Actions import draw as dra
from Actions import mouse_picking
from Actions.character import create_character
from Actions.billy import Snowman
from Actions.enemy import create_enemy
from Actions.pantalla_titulo import PantallaTitulo as pantalla
from Actions import escenarios as es
from Actions import posiciones
from Actions.game_level import GameLevel, GameState
from Actions import preguntas
from Actions.preguntas import JuegoPreguntas
from Actions import game_state_manager
from Actions.game_state_manager import GameStateManager, GameStatus
from Fondos import *
from Sounds import *
import tkinter as tk
from tkinter import messagebox
from tkinter import simpledialog
import pyttsx3



# Autores: Jorge Ortiz Ceballos e Iñaki Iturriaga Rabanal
# Fecha: 24/11/2024
# Descripción: Programa juego de aventura educativa en 3D con preguntas y respuestas.

directorio_script = os.path.dirname(os.path.abspath(__file__))

camera_speed = 0.1
rotacion_speed = 0.2
mouse_sensivity = 0.1

rotation_angle_start = 0.0  # Ángulo inicial de rotación
rotation_speed_start = 1.0   # Velocidad de rotación (grados por frame)

pygame.event.set_grab(True)
pygame.mouse.set_visible(True)

tiempo2 = 0

# Lista de escenarios y sonidos
escenarios = [os.path.join('Fondos', f) for f in ['select.jpg', '01.jpg', '02.jpg', '03.jpeg', '04.jpeg', '05.jpg', '06.jpeg', '07.jpeg', '08.jpg', '09.jpeg', '10.jpg', '11.jpg', '12.jpg', '13.jpg', '14.jpg', '15.jpg']]
sonidos = [os.path.join('Sounds', f) for f in ['s00.mp3', 's01.mp3', 's02.mp3', 's03.mp3', 's04.mp3', 's05.mp3', 's06.mp3', 's07.mp3', 's08.mp3', 's09.mp3', 's10.mp3', 's11.mp3', 's12.mp3', 's13.mp3', 's14.mp3', 's15.mp3', 's16.mp3', 's17.mp3', 's18.mp3', 's19.mp3', 's20.mp3', 's21.mp3']]

current_escenario = 0
current_level = 1

# Posiciones de los objetos
PosX_objeto4 = 10
PosY_objeto4 = 5
PosZ_objeto4 = 14
obj4_height = 1

PosX_objeto3 = 5
PosY_objeto3 = 5
PosZ_objeto3 = 14
obj3_height = 5

PosX_objeto2 = 0
PosY_objeto2 = 0
PosZ_objeto2 = 14
obj2_height = 1

PosX_objeto1 = 20
PosY_objeto1 = 30
PosZ_objeto1 = 15
objeto1_height = 1
objeto1_width = 1
objeto1_depth = 1


PosX_objeto = 6
PosY_objeto = 6
PosZ_objeto = 4
objeto_height = 1
objeto_width = 1
objeto_depth = 1

def draw5():        
    glEnable(GL_DEPTH_TEST)
    glPushMatrix()
    glTranslatef(PosX_objeto4, PosY_objeto4, PosZ_objeto4)
    lc.interpolado(0.4, 0.4, 0.4)
    glColor3b(255, 165, 0)
    obj.draw_pyramid(3, 6, 0, 2)
    glPopMatrix()
    glDisable(GL_LIGHTING)
    glDisable(GL_LIGHT0)

def draw4():        
    glEnable(GL_DEPTH_TEST)
    glPushMatrix()
    glTranslatef(5, 5, PosZ_objeto3)
    lc.gouraud(0.6, 0.6, 0.6)
    glColor3b(45,87,44)
    obj.draw_cube_dos()
    glPopMatrix()
    glDisable(GL_LIGHTING)
    glDisable(GL_LIGHT0)

def draw3():
    
    glEnable(GL_DEPTH_TEST)
    glPushMatrix()
    glTranslatef(PosX_objeto2, PosY_objeto2, PosZ_objeto2)
    lc.phong(1.8, 1.8, 1.8)
    obj.draw_cube_dos()
    glPopMatrix()
    glDisable(GL_LIGHTING)
    glDisable(GL_LIGHT0)

def draw2(movX, movY):
    global PosX_objeto1, PosY_objeto1
    
    ancho_pantalla = 800  # Cambia por el ancho real de tu espacio
    alto_pantalla = 600   # Cambia por el alto real de tu espacio

    PosX_objeto1 += movX
    PosY_objeto1 += movY

    PosX_objeto1 = max(0, min(PosX_objeto1, ancho_pantalla))
    PosY_objeto1 = max(0, min(PosY_objeto1, alto_pantalla))

    
    
    glEnable(GL_DEPTH_TEST)
    glPushMatrix()
    glTranslatef(PosX_objeto1, PosY_objeto1, PosZ_objeto1)

    lc.phong(0.8, 0.8, 0.8)
    obj.draw_cube_dos()
    glPopMatrix()
    glDisable(GL_LIGHTING)
    glDisable(GL_LIGHT0)

# Dibuja el personaje y aplica iluminación
def draw(character):
    glEnable(GL_DEPTH_TEST)
    glPushMatrix()
    glTranslatef(PosX_objeto, PosY_objeto, PosZ_objeto)

    
    character.draw()  # Llama al método `draw()` del personaje
    glPopMatrix()
    glDisable(GL_LIGHTING)
    glDisable(GL_LIGHT0)

def show_message_window(message):
    root = tk.Tk()
    root.withdraw()
    messagebox.showinfo("Mensaje", message)
    root.destroy()

def show_menu():
    txt.draw_text_3d("Menu", 5, 20, 0, 20, 255, 255, 255, 0, 0, 0)
    txt.draw_text_3d("Elige un personaje", 5, 18, 0, 20, 255, 255, 255, 0, 0, 0)
    txt.draw_text_3d("Presiona 1 para Perfumin", 5, 17, 0, 20, 255, 255, 255, 0, 0, 0)
    txt.draw_text_3d("Presiona 2 para Billy Jean", 5, 16, 0, 20, 255, 255, 255, 0, 0, 0)
    txt.draw_text_3d("Presiona 3 para Enemy", 5, 15, 0, 20, 255, 255, 255, 0, 0, 0)
    txt.draw_text_3d("Presiona Z para Comenzar Partida", 5, 14, 0, 20, 255, 255, 255, 0, 0, 0)

def show_personaje():
    # Perfuminbb
    txt.draw_text("Perfumin", 5, 12, 0, 20, 255, 255, 255, 0, 0, 0)  # Título de Perfumin
    txt.draw_text("Astuto y curioso. Frágil ante el daño.", 5, 10, 0, 20, 255, 255, 255, 0, 0, 0)  # Descripción de Perfumin

    # Billy Bean
    txt.draw_text("Billy Bean", 5, 8, 0, 20, 255, 255, 255, 0, 0, 0)  # Título de Billy Bean
    txt.draw_text("Resiliente y enérgico.", 5, 7, 0, 20, 255, 255, 255, 0, 0, 0)  # Descripción de Billy Bean
    txt.draw_text("Alta resistencia ante el daño menos al fuego.", 5, 6, 0, 20, 255, 255, 255, 0, 0, 0)  # Descripción de Billy Bean
    # Enemy
    txt.draw_text("Enemy", 5, 4, 0, 20, 255, 255, 255, 0, 0, 0)  # Título de Enemy
    txt.draw_text("Alta Dificultad.", 5, 3, 0, 20, 255, 255, 255, 0, 0, 0)  # Descripción de Enemy
    txt.draw_text("Su resistencia media es clave.", 5, 2, 0, 20, 255, 255, 255, 0, 0, 0)  # Descripción de Enemy

def show_personaje_individual(action):
    if action == 1:
        # Perfumin
        txt.draw_text("Perfumin", 5, 12, 0, 20, 255, 255, 255, 0, 0, 0)  # Título de Perfumin
        txt.draw_text("Astuto y curioso. Frágil ante el daño.", 5, 10, 0, 20, 255, 255, 255, 0, 0, 0)  # Descripción de Perfumin
        
    elif action == 2:
        # Billy Bean
        txt.draw_text("Billy Bean", 5, 8, 0, 20, 255, 255, 255, 0, 0, 0)  # Título de Billy Bean
        txt.draw_text("Resiliente y enérgico.", 5, 7, 0, 20, 255, 255, 255, 0, 0, 0)  # Descripción de Billy Bean
        txt.draw_text("Alta resistencia ante el daño menos al fuego.", 5, 6, 0, 20, 255, 255, 255, 0, 0, 0)  # Descripción de Billy Bean
    elif action == 3:
        # Enemy
        txt.draw_text("Enemy", 5, 4, 0, 20, 255, 255, 255, 0, 0, 0)  # Título de Enemy
        txt.draw_text("Alta Dificultad.", 5, 3, 0, 20, 255, 255, 255, 0, 0, 0)  # Descripción de Enemy
        txt.draw_text("Su resistencia media es clave.", 5, 2, 0, 20, 255, 255, 255, 0, 0, 0)  # Descripción de Enemy


def init_gl():
    glEnable(GL_DEPTH_TEST)  # Habilita el test de profundidad
    glClearColor(1.0, 0.0, 0.0, 1.0)  # Establece el color de fondo
    # Configuración de iluminación
    glEnable(GL_LIGHTING)
    glEnable(GL_LIGHT0)
    glEnable(GL_COLOR_MATERIAL)
    glEnable(GL_DEPTH_TEST)
    glEnable(GL_NORMALIZE)

    # Configura la posición de la luz
    glLightfv(GL_LIGHT0, GL_POSITION, [1.0, 1.0, 1.0, 0.0])

    # Configura las propiedades del material
    glMaterialfv(GL_FRONT, GL_AMBIENT, [0.2, 0.2, 0.2, 1.0])
    glMaterialfv(GL_FRONT, GL_DIFFUSE, [0.8, 0.8, 0.8, 1.0])


def on_success():
    print("Respuesta correcta")
    show_message_window("Respuesta correcta")
    return True

def on_failure():
    print("Respuesta incorrecta")
    show_message_window("Respuesta incorrecta")
    return False

def check_game_status(correct_answers, incorrect_answers):
    """
    Verifica el estado del juego basado en respuestas correctas e incorrectas.
    Retorna una tupla con: (continúa_juego, nuevo_nivel, mensaje)
    """
    
    # Verificar game over por respuestas incorrectas
    if incorrect_answers >= 2:
        show_message_window("Has perdido. Demasiadas respuestas incorrectas.")  
        return False, False, "Has perdido. Demasiadas respuestas incorrectas."
        pygame.quit()
    
    # Verificar progreso según el nivel actual
    if correct_answers < 3:
        current_level = 1
    if correct_answers >= 3 and correct_answers < 6:
        current_level = 2
    if correct_answers >= 6 and correct_answers < 9:
        current_level = 3
    
    if current_level == 1 and correct_answers > 3:        
        incorrect_answers = 0
        current_level = 2
        son.play_sound("Sounds/level_change.mp3") 
        current_escenario = (current_escenario + 1) % len(escenarios)
        show_message_window("Has completado el nivel 1.")
        return False, True, "Has completado el nivel 1."        
    
    elif current_level == 2 and correct_answers > 6:
        incorrect_answers = 0
        son.play_sound("Sounds/level_change.mp3") 
        current_escenario = (current_escenario + 1) % len(escenarios)
        current_level = 3
        show_message_window("Has completado el nivel 2.")
        return False, True, "Has completado el nivel 2."
        
    elif current_level == 3 and correct_answers > 9:
        son.play_sound("Sounds/level_1.mp3")
        show_message_window("Has completado el nivel 3.")
        return False, True, "Has completado el nivel 3."
    
def pedir_nombre():
    """
    Abre una ventana para que el usuario ingrese su nombre y lo retorna.
    """
    ventana = tk.Tk()
    ventana.withdraw()  # Ocultar la ventana principal
    nombre = simpledialog.askstring("Nombre", "Por favor, ingresa tu nombre:")  # Solicitar nombre
    ventana.destroy()  # Cerrar ventana
    return nombre

def reproducir_texto(nombre):
    """
    Usa pyttsx3 para convertir texto a voz, incluyendo el nombre ingresado.
    """
    # Inicializar el motor de voz
    engine = pyttsx3.init()

    # Texto personalizado con el nombre
    texto = f"Hola {nombre}, estas en aventura del conocimiento, ¡es hora de aprender!."

    # Configurar y reproducir
    engine.setProperty('rate', 150)  # Velocidad de la voz
    engine.setProperty('volume', 0.9)  # Volumen de la voz
    engine.say(texto)
    engine.runAndWait()    
    
def show_restart_menu():
    root = tk.Tk()
    root.withdraw()  # Ocultar la ventana principal
    response = messagebox.askyesno("Reiniciar", "Game Over! ¿Te gustaría reiniciar el juego?")
    root.destroy()  # Cerrar la ventana principal
    return response  # Devuelve True si el usuario elige "Sí", False si elige "No"

def main():
    global continua_juego, current_escenario, elapsed_time, action, rotation_angle_start, rotation_speed_start , move_count, rotation_complete, current_level  # Declaración global

    pygame.init()
    pygame.mixer.init()

    display = (800, 600)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
    pygame.display.set_caption("Aventura del Conocimiento")

    gluPerspective(45, (display[0] / display[1]), 0.1, 50.0)
    glTranslatef(0.0, 0.0, -5)
    glOrtho(0, 15, 0, 15, 0, 6)

    character = create_character # Usamos la instancia importada
    enemy = create_enemy
    snowman = Snowman()    
    elapsed_time = 0  # Inicializamos la variable aquí
    action = 0
    rotation_angle_character = 0.0  # Ángulo de rotación del personaje
    rotation_speed_char = 2.0
    move_count = 0
    game_positions = GamePositions()

    correct_answers = 0  # Respuestas correctas acumuladas
    incorrect_answers = 0  # Respuestas incorrectas en el nivel actual
    continua_juego = True
    

    pygame.mouse.set_visible(False)
    pygame.event.set_grab(True)
    son.play_music("Sounds/principal1.mp3")

    # Configuración de iluminación y otros ajustes de OpenGL
    init_gl()

    elapsed_time += 0.1  # Ahora la variable `elapsed_time` está definida
    running = True
    paused = True
    rotation_complete = False

    instructions = [
        "Controles básicos:",
        "- Flecha izquierda (←): Mover a la izquierda.",
        "- Flecha derecha (→): Mover a la derecha.",
        "- Flecha arriba (↑): Mover hacia adelante (eje Z).",
        "- Flecha abajo (↓): Mover hacia atrás (eje Z).",
        "- Espacio: Subir (saltar).",
        "- Tecla N: Bajar (agacharse).",
        "- Tecla K: Patear.",
        "- Tecla H: Saludar o levantar los brazos.",
        "",
        "Controles específicos por personaje:",
        "- Personaje 1: Controlado por las teclas especificadas.",
        "- Personaje 2: Snowman con movimientos similares.",
        "- Personaje 3: Enemy también usa las mismas teclas.",
        "",
        "Presiona ESC para salir de este menú."
    ]
    
    game_state = GameState.CHARACTER_SELECT
    game_level = GameLevel()
    current_level = 1
    game_manager = GameStateManager()
    juego = JuegoPreguntas(on_success, on_failure)
    nombre = pedir_nombre()
    bandera = True

    while running:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                quit()

        rotation_angle_start += rotation_speed_start
        rotation_angle_character += rotation_speed_char

        if rotation_angle_start >= 180:  # Resetea el ángulo después de completar una vuelta
            rotation_angle_start = 180
            rotation_complete = True

        # Incrementa los ángulos de rotación
        if rotation_angle_character >= 180:  # Detener después de 180 grados
            rotation_angle_character = 180

        if rotation_angle_start >= 180 and move_count < 100:
            glTranslatef(camera_speed, 0, 0)
            move_count += 1

        # Limpia el buffer de la pantalla
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        # Aplica la rotación sobre el eje X
        glPushMatrix()  # Guarda la matriz actual
        glRotatef(rotation_angle_start, 0, 1, 0)  # Rota sobre el eje Y

        # Limpia el buffer de la pantalla

        es.draw_escenario(escenarios[current_escenario])  # Dibuja el escenario actual
        glPopMatrix()

        keys = pygame.key.get_pressed()
        # Movimiento de la cámara
        if keys[pygame.K_w]:
            glTranslatef(0, -camera_speed, 0)
        if keys[pygame.K_s]:
            glTranslatef(0, camera_speed, 0)
        if keys[pygame.K_a]:
            glTranslatef(camera_speed, 0, 0)
        if keys[pygame.K_d]:
            glTranslatef(-camera_speed, 0, 0)
        if keys[pygame.K_q]:
            glTranslatef(0, 0, camera_speed)  # Zoom in
        if keys[pygame.K_e]:
            glTranslatef(0, 0, -camera_speed)  # Zoom out

        # Rotación con el ratón
        x, y = pygame.mouse.get_rel()
        x *= mouse_sensivity
        y *= mouse_sensivity

        if x != 0:
            glRotatef(x, 0, 1, 0)
        if y != 0:
            glRotatef(y, 1, 0, 0)

        pygame.mouse.set_pos(display[0] // 2, display[1] // 2)

        
        if paused:  # Si está en pausa, solo espera a que se presione 'P'
            if keys[pygame.K_p]:
                paused = False  # Cambia el estado a no pausado
                continue  # Salta el resto del ciclo y evita dibujar cosas

        glPushMatrix()
        glRotatef(rotation_angle_character, 0, 1, 0)
        dra.draw_character(character, 12, 6, 4)
        dra.draw_character(snowman, 6, 6, 4)
        dra.draw_character(enemy, 0, 6, 4)
        character.jump()
        snowman.jump()
        enemy.jump()
        
        glPopMatrix()

        if rotation_complete:
            show_menu()
            show_personaje()

        

        if game_state == GameState.CHARACTER_SELECT:
            if keys[pygame.K_1]:
                action = 1
                son.play_sound("Sounds/pick.mp3")
                character.set_expression('smile')
                character.raise_left_arm()
                character.raise_right_arm()
                snowman.crouch()
                snowman.set_expression("frown")
                enemy.lie_down()
                enemy.set_expression('sad')
                show_message_window("Elegiste a Perfumin")
                paused = True
            elif keys[pygame.K_2]:
                action = 2
                son.play_sound("Sounds/pick.mp3")
                snowman.wave()
                snowman.set_expression('smile')
                character.crouch()
                character.set_expression('sad')
                enemy.lie_down()
                enemy.set_expression('sad')
                show_message_window("Elegiste a Billy Bean")
                paused = True
            elif keys[pygame.K_3]:
                action = 3
                son.play_sound("Sounds/pick.mp3")
                enemy.jump()
                enemy.set_expression('smile')
                snowman.crouch()
                snowman.set_expression('frown')
                character.lie_down()
                character.set_expression('sad')
                show_message_window("Elegiste a Enemy")
                paused = True

            elif keys[pygame.K_z] and action != 0:
                character.reset()
                snowman.reset()
                enemy.reset()
                son.play_sound("Sounds/start01.mp3")
                game_state = GameState.PLAYING_LEVEL
                game_level.initialize_level(action)
                current_escenario = 1  # Cambiar al escenario del primer nivel
                snowman.remove()
                character.remove()
                enemy.remove()
                son.play_music("Sounds/game-music-loop-1-143979.mp3")
                
            
        elif game_state == GameState.PLAYING_LEVEL:
            glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
            
            

            # Dibujar escenario
            es.draw_escenario(escenarios[current_escenario])

            while bandera:
                reproducir_texto(nombre)
                bandera = False


            # Dibujar nivel
            game_level.draw_level(action)
            # Dibujar personaje seleccionado
            

            # Manejar movimiento y actualizar nivel
            game_level.handle_movement(keys, action)
            game_level.update()

            
                
            
            draw3()
            draw4()
            draw5()

            keys = pygame.key.get_pressed()
            if keys[pygame.K_j]:
                draw2(-1,0)
            if keys[pygame.K_l]:
                draw2(1,0)
            if keys[pygame.K_i]:
                draw2(0,1)
            if keys[pygame.K_k]:
                draw2(0,-1)
            if keys[pygame.K_F3]:
                show_personaje_individual(action)
            if keys[pygame.K_F4]:
                if action == 1:
                    character.reset()
                if action == 2:
                    snowman.reset()
                if action == 3:
                    enemy.reset() 

            

            if coli.rombo_collision(
                PosX_objeto1,
                PosY_objeto1,
                PosZ_objeto1,
                objeto1_width,
                objeto1_height,
                objeto1_depth,
                PosX_objeto2,
                PosY_objeto2,
                PosZ_objeto2,
                obj2_height
        ):
                pygame.mouse.set_visible(True)
                son.play_sound("Sounds/s06.mp3")
                juego.seleccionar_pregunta()
                draw2(30.0, 30.0)
                resultado = juego.obtener_resultado()

                status, message = game_manager.record_answer(resultado)


                if resultado:
                    son.play_sound("Sounds/start.mp3")
                    correct_answers += 1
                else:
                    son.play_sound("Sounds/wrong.mp3")
                    incorrect_answers += 1
                
                  # Handle the game status
                if status == GameStatus.GAME_OVER:
                    show_message_window(message)
                    action = 0
                    running = False
                elif status == GameStatus.LEVEL_COMPLETE:
                    game_manager.advance_level()
                    current_level = game_manager.current_level
                    current_escenario = (current_escenario + 1) % len(escenarios)
                    son.play_sound("Sounds/level_change.mp3")
                    show_message_window(message)
                elif status == GameStatus.GAME_WIN:
                    show_message_window(message)
                    action = 0
                    running = False
                
                # Show progress after each answer (optional)
                if keys[pygame.K_TAB]:  # Add a key to show progress
                    progress_report = game_manager.get_progress_report()
                    show_message_window(progress_report)
            
            if coli.rombo_collision_dos(
                PosX_objeto1,
                PosY_objeto1,
                PosZ_objeto1,
                objeto1_width,
                objeto1_height,
                objeto1_depth,
                PosX_objeto3,
                PosY_objeto3,
                PosZ_objeto3,
                obj3_height
            ):
                pygame.mouse.set_visible(True)
                son.play_sound("Sounds/s06.mp3")
                juego.seleccionar_pregunta()
                draw2(30.0, 30.0)
                resultado = juego.obtener_resultado()

                status, message = game_manager.record_answer(resultado)


                if resultado:
                    son.play_sound("Sounds/start.mp3")
                    correct_answers += 1
                else:
                    son.play_sound("Sounds/wrong.mp3")
                    incorrect_answers += 1
                
                  # Handle the game status
                if status == GameStatus.GAME_OVER:
                    show_message_window(message)
                    running = False
                elif status == GameStatus.LEVEL_COMPLETE:
                    game_manager.advance_level()
                    current_level = game_manager.current_level
                    current_escenario = (current_escenario + 1) % len(escenarios)
                    son.play_sound("Sounds/level_change.mp3")
                    show_message_window(message)
                elif status == GameStatus.GAME_WIN:
                    show_message_window(message)
                    running = False
                
                # Show progress after each answer (optional)
                if keys[pygame.K_TAB]:  # Add a key to show progress
                    progress_report = game_manager.get_progress_report()
                    show_message_window(progress_report)

            if coli.rombo_collision_dos(
                PosX_objeto1,
                PosY_objeto1,
                PosZ_objeto1,
                objeto1_width,
                objeto1_height,
                objeto1_depth,
                PosX_objeto4,
                PosY_objeto4,
                PosZ_objeto4,
                obj4_height
            ):
                pygame.mouse.set_visible(True)
                son.play_sound("Sounds/s06.mp3")
                juego.seleccionar_pregunta()
                draw2(30.0, 30.0)
                resultado = juego.obtener_resultado()

                status, message = game_manager.record_answer(resultado)


                if resultado:
                    son.play_sound("Sounds/start.mp3")
                    correct_answers += 1
                else:
                    son.play_sound("Sounds/wrong.mp3")
                    incorrect_answers += 1
                
                  # Handle the game status
                if status == GameStatus.GAME_OVER:
                    show_message_window(message)
                    running = False
                elif status == GameStatus.LEVEL_COMPLETE:
                    game_manager.advance_level()
                    current_level = game_manager.current_level
                    current_escenario = (current_escenario + 1) % len(escenarios)
                    son.play_sound("Sounds/level_change.mp3")
                    show_message_window(message)
                elif status == GameStatus.GAME_WIN:
                    show_message_window(message)
                    running = False
                
                # Show progress after each answer (optional)
                if keys[pygame.K_TAB]:  # Add a key to show progress
                    progress_report = game_manager.get_progress_report()
                    show_message_window(progress_report)

             

        # Cambiar escenario
        if keys[pygame.K_c]:
            current_escenario = (current_escenario + 1) % len(escenarios)
        # Sonido general
        if keys[pygame.K_v]:  # Encender sonido general
            son.play_music("Sounds/s00.mp3")
        if keys[pygame.K_b]:  # Apagar sonido general
            son.stop_music()

        # Mostrar instrucciones al presionar F1

        if keys[pygame.K_F1]:
            show_message_window(instructions)
        if keys[pygame.K_F2]:
            show_message_window("Desarrollado por: Iñaki Iturriaga Rabanal y Jorge Ortiz Ceballos")
        if keys[pygame.K_ESCAPE]:
            running = False
            quit()

        clock = pygame.time.Clock()
        clock.tick(60)

        pygame.display.flip()
        pygame.time.wait(10)

    pygame.quit()

if __name__ == "__main__":
    pantalla_uno =  pantalla()

    while True:
        if pantalla_uno.ejecutar():
            while True:
                main()

                user_choice = show_restart_menu()
                if not user_choice:
                    break  # Salir del juego si el usuario elige salir