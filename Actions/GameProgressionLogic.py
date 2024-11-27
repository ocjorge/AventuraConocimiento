class GameProgression:
    def __init__(self):
        self.level = 1
        self.total_correct = 0
        self.incorrect_current_level = 0
        self.required_correct = {
            1: 3,  # Nivel 1 requiere 3 correctas
            2: 6,  # Nivel 2 requiere 6 correctas acumuladas
            3: 9   # Nivel 3 requiere 9 correctas acumuladas
        }
        
    def check_progression(self, correct_answers, incorrect_answers):
        """
        Verifica la progresión del juego basado en respuestas correctas e incorrectas
        
        Returns:
            tuple: (game_over, level_up, message)
        """
        self.total_correct = correct_answers
        self.incorrect_current_level = incorrect_answers
        
        # Verifica si perdió el nivel actual
        if self.incorrect_current_level >= 2:
            return True, False, "¡Has perdido! Contestaste mal 2 preguntas en este nivel."
            
        # Verifica si pasó al siguiente nivel
        if self.level <= 3 and self.total_correct >= self.required_correct[self.level]:
            old_level = self.level
            self.level += 1
            self.incorrect_current_level = 0  # Reinicia contador de incorrectas
            
            if self.level > 3:
                return True, False, "¡Felicidades! ¡Has completado todos los niveles!"
            else:
                return False, True, f"¡Felicidades! Avanzas al nivel {self.level}"
                
        return False, False, ""
        
    def get_progress(self):
        """
        Retorna el progreso actual del jugador
        """
        return {
            'nivel_actual': self.level,
            'correctas_totales': self.total_correct,
            'incorrectas_nivel': self.incorrect_current_level,
            'correctas_necesarias': self.required_correct[self.level]
        }

def on_success():
    global current_level, juego_preguntas
    game_progress = GameProgression()
    game_over, level_up, message = game_progress.check_progression(
        juego_preguntas.puntuacion_correcta,
        juego_preguntas.puntuacion_incorrecta
    )
    
    if game_over:
        son.play_sound("Sounds/level_1.mp3")
        show_message_window(message)
        pygame.quit()
        quit()
    elif level_up:
        current_level = game_progress.level
        son.play_music("Sounds/level_change.mp3")
        show_message_window(message)
        juego_preguntas.puntuacion_incorrecta = 0  # Reinicia incorrectas para el nuevo nivel

def on_failure():
    global running, current_level
    game_progress = GameProgression()
    game_over, _, message = game_progress.check_progression(
        juego_preguntas.puntuacion_correcta,
        juego_preguntas.puntuacion_incorrecta
    )
    
    if game_over:
        son.play_sound("Sounds/over.mp3")
        show_message_window(message)
        running = False