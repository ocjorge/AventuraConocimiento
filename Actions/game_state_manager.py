# game_state_manager.py
import logging
from enum import Enum

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class GameStatus(Enum):
    CONTINUE = "CONTINUE"
    LEVEL_COMPLETE = "LEVEL_COMPLETE"
    GAME_OVER = "GAME_OVER"
    GAME_WIN = "GAME_WIN"

class GameStateManager:
    def __init__(self):
        self.current_level = 1
        self.correct_answers = 0
        self.incorrect_answers = 0
        self.max_incorrect_per_level = 2
        self.answers_to_advance = {
            1: 3,  # Need 3 correct answers to complete level 1
            2: 6,  # Need 6 total correct answers to complete level 2
            3: 9   # Need 9 total correct answers to complete level 3
        }
        
    def record_answer(self, is_correct):
        """Guarda una respuesta correcta o incorrecta y verifica el estado del juego."""
        if is_correct:
            self.correct_answers += 1
            logger.info(f"Respuesta correcta registrada! Total correctas: {self.correct_answers}")
            
        else:
            self.incorrect_answers += 1
            logger.info(f"Respuesta incorrecta registrada! Total incorrectas: {self.incorrect_answers}")
            
        
        return self.check_game_status()
    
    def check_game_status(self):
        """
        revisa el estado actual del juego basado en las respuestas y niveles.
        Devuelve una tupla de (GameStatus, str) que contiene el estado y un mensaje.       
        """
        # Log current state
        logger.info(f"""
        Current game state:
        - Level: {self.current_level}
        - Correct answers: {self.correct_answers}
        - Incorrect answers: {self.incorrect_answers}
        - Required answers for current level: {self.answers_to_advance.get(self.current_level)}
        """)
        
        # Check for game over
        if self.incorrect_answers >= self.max_incorrect_per_level:
            return (GameStatus.GAME_OVER,
                    f"Game Over! Demasiadas respuestas incorrectas ({self.incorrect_answers})") 
                   
        
        # Check for level completion
        required_answers = self.answers_to_advance.get(self.current_level)
        if self.correct_answers >= required_answers:
            if self.current_level == 3:
                return (GameStatus.GAME_WIN, 
                        f"¡Felicidades! ¡Has completado todos los niveles con {self.correct_answers} respuestas correctas!")
                       
            else:
                next_level = self.current_level + 1
                return (GameStatus.LEVEL_COMPLETE, 
                        f"Nivel {self.current_level} completado! Pasando al nivel {next_level}")
                       
        
        return (GameStatus.CONTINUE,
                f"Continua jugando el nivel {self.current_level}") 
               
    
    def advance_level(self):
        """Avanza al siguiente nivel y reinicia las respuestas incorrectas"""
        
        if self.current_level < 3:
            self.current_level += 1
            self.incorrect_answers = 0
            logger.info(f"Advanced to level {self.current_level}")
            
    def get_progress_report(self):
        """Obtiene un informe detallado del progreso"""
        
        return f"""
        Game Progress Report:
        -------------------
        Current Level: {self.current_level}
        Total Correct Answers: {self.correct_answers}
        Incorrect Answers (this level): {self.incorrect_answers}
        Answers Needed for Next Level: {self.answers_to_advance.get(self.current_level) - self.correct_answers}
        Max Incorrect Allowed: {self.max_incorrect_per_level}
        """