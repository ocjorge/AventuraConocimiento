# sonidos.py
import pygame as py

# Inicialización del módulo de sonidos
py.init()
py.mixer.init()

def play_music(filename, loop=-1):
    """Reproduce una música de fondo.

    Args:
        filename: El nombre del archivo de la música.
        loop: Número de veces que se repetirá (por defecto, -1 para bucle infinito).
    """
    try:
        py.mixer.music.load(filename)
        py.mixer.music.play(loop)
    except py.error as e:
        print(f"Error al reproducir la música: {e}")

def stop_music():
    """Detiene la música actual."""
    py.mixer.music.stop()

def play_sound(filename):
    """Reproduce un efecto de sonido.

    Args:
        filename: El nombre del archivo del efecto de sonido.
    """
    try:
        sound = py.mixer.Sound(filename)
        sound.play()
    except py.error as e:
        print(f"Error al reproducir el sonido: {e}")

def set_music_volume(volume):
    """Ajusta el volumen de la música de fondo.

    Args:
        volume: Un valor entre 0.0 (silencio) y 1.0 (volumen máximo).
    """
    py.mixer.music.set_volume(volume)

def set_sound_volume(sound, volume):
    """Ajusta el volumen de un efecto de sonido.

    Args:
        sound: El objeto de sonido que se quiere ajustar.
        volume: Un valor entre 0.0 (silencio) y 1.0 (volumen máximo).
    """
    sound.set_volume(volume)