#preguntas.py
import tkinter as tk
import random
import pygame

class JuegoPreguntas:
    def __init__(self, on_success, on_failure):
        """Inicializa las preguntas, respuestas y puntuación."""
        self.on_success = on_success
        self.on_failure = on_failure
       
        self.preguntas = [
            # Historia
            "¿En qué año Cristóbal Colón llegó a América?",
            "¿Quién fue el primer presidente de México?",
            "¿Qué civilización construyó las pirámides de Teotihuacán?",
            "¿En qué año se independizó México de España?",
            "¿Qué cultura mesoamericana creó el calendario azteca?",
            "¿Quién fue Benito Juárez?",
            "¿Cuál fue la primera civilización de América?",
            "¿Qué acontecimiento histórico ocurrió en México en 1910?",
            "¿Quién fue Sor Juana Inés de la Cruz?",
            "¿Qué significó la Guerra de los Pasteles para México?",
            "¿Qué fue el Grito de Dolores?",
            "¿Quién fue Miguel Hidalgo y Costilla?",
            "¿Quién lideró la toma de la Alhóndiga de Granaditas?",
            "¿Qué tratado puso fin a la Guerra de Independencia de México?",

            # Geografía
            "¿Cuál es el río más largo de México?",
            "¿Qué estados de México colindan con Estados Unidos?",
            "¿Cuál es el volcán más alto de México?",
            "¿En qué estado se encuentra Chichén Itzá?",
            "¿Cuál es la capital de Jalisco?",
            "¿Qué tipo de clima predomina en el norte de México?",
            "¿Cuál es el lago más grande de México?",
            "¿En qué estado se encuentra el Cañón del Sumidero?",
            "¿Qué mar baña las costas orientales de México?",
            "¿Cuál es la península más grande de México?",
            "¿En qué estado se encuentra el desierto de Sonora?",
            "¿Qué estados conforman la península de Yucatán?",
            "¿Cuál es la montaña más alta de México después del Pico de Orizaba?",
            "¿En qué estado de México se encuentra la Reserva de la Biósfera Calakmul?",

            # Ciencia
            "¿Qué es la fotosíntesis?",
            "¿Cuáles son los estados de la materia?",
            "¿Qué es el sistema solar?",
            "¿Qué son los huesos?",
            "¿Cómo se llaman las células que transportan oxígeno en la sangre?",
            "¿Qué es el ciclo del agua?",
            "¿Qué son los ecosistemas?",
            "¿Cuál es la función principal del corazón?",
            "¿Qué es la cadena alimenticia?",
            "¿Qué son las placas tectónicas?",
            "¿Qué es la fuerza de gravedad?",
            "¿Cuáles son las capas de la Tierra?",
            "¿Cuál es el órgano más grande del cuerpo humano?",
            "¿Qué gas es esencial para la respiración?",

            # Cultura Popular
            "¿Quién es Pedro Infante?",
            "¿Qué es el Día de Muertos?",
            "¿Cuál es el platillo más representativo de México?",
            "¿Qué son los alebrijes?",
            "¿Qué es la Guelaguetza?",
            "¿Qué es un mariachi?",
            "¿Cuál es el deporte más popular en México?",
            "¿Qué son las piñatas?",
            "¿Qué es el Jarabe Tapatío?",
            "¿Qué es una trajinera?",
            "¿Qué son los mexicas?",
            "¿Qué es el Popol Vuh?",
            "¿Qué representa un altar de Día de Muertos?",
            "¿Qué significa la palabra 'Xoloitzcuintle'?"
        ]

        self.respuestas_correctas = [
            # Historia
            "1492",
            "Guadalupe Victoria",
            "Teotihuacanos",
            "1821",
            "Azteca",
            "Presidente de México y defensor de la República",
            "Olmeca",
            "La Revolución Mexicana",
            "Una poetisa y escritora del siglo XVII",
            "Un conflicto entre México y Francia",
            "El inicio de la Independencia de México",
            "El padre de la patria mexicana",
            "Miguel Hidalgo",
            "Tratado de Córdoba",

            # Geografía
            "Río Bravo",
            "Baja California, Sonora, Chihuahua, Coahuila, Nuevo León y Tamaulipas",
            "Pico de Orizaba",
            "Yucatán",
            "Guadalajara",
            "Árido y semiárido",
            "Lago de Chapala",
            "Chiapas",
            "Golfo de México",
            "Península de Yucatán",
            "Sonora",
            "Campeche, Yucatán y Quintana Roo",
            "Popocatépetl",
            "Campeche",

            # Ciencia
            "Proceso por el que las plantas producen su alimento",
            "Sólido, líquido y gaseoso",
            "Conjunto de planetas que giran alrededor del Sol",
            "Tejido que forma el esqueleto",
            "Glóbulos rojos",
            "Proceso de transformación del agua en la naturaleza",
            "Comunidades de seres vivos y su ambiente",
            "Bombear sangre por todo el cuerpo",
            "Relación alimentaria entre seres vivos",
            "Fragmentos de la corteza terrestre",
            "Fuerza que atrae los objetos hacia el centro de la Tierra",
            "Corteza, manto y núcleo",
            "La piel",
            "Oxígeno",

            # Cultura Popular
            "Un famoso actor y cantante mexicano",
            "Celebración tradicional mexicana para recordar a los difuntos",
            "Los tacos",
            "Artesanías mexicanas de criaturas fantásticas",
            "Festival cultural de Oaxaca",
            "Grupo musical tradicional mexicano",
            "El fútbol",
            "Artesanías para fiestas llenas de dulces",
            "Baile folclórico mexicano",
            "Embarcación típica de Xochimilco",
            "Pueblo indígena que fundó Tenochtitlan",
            "Libro sagrado de los mayas",
            "Un homenaje a los difuntos",
            "Perro sin pelo mexicano"
        ]

        self.respuestas_incorrectas = [
            # Historia
            ["1489", "1495", "1500"],
            ["Benito Juárez", "Porfirio Díaz", "Antonio López de Santa Anna"],
            ["Mayas", "Aztecas", "Olmecas"],
            ["1810", "1824", "1836"],
            ["Maya", "Olmeca", "Tolteca"],
            ["Un conquistador español", "Un artista colonial", "Un revolucionario"],
            ["Maya", "Azteca", "Tolteca"],
            ["La Independencia", "La Reforma", "La Guerra con Estados Unidos"],
            ["Una revolucionaria", "Una pintora", "Una emperatriz"],
            ["Una batalla con España", "Un conflicto con Inglaterra", "Una guerra civil"],
            ["Una batalla importante", "Un tratado de paz", "Una reforma política"],
            ["Un virrey", "Un revolucionario", "Un presidente"],
            ["José María Morelos", "Vicente Guerrero", "Agustín de Iturbide"],
            ["Plan de Iguala", "Plan de Ayala", "Plan de San Luis"],

            # Geografía
            ["Río Lerma", "Río Balsas", "Río Grijalva"],
            ["Solo Chihuahua y Sonora", "Todo el norte de México", "Tres estados fronterizos"],
            ["Popocatépetl", "Iztaccíhuatl", "Nevado de Toluca"],
            ["Quintana Roo", "Campeche", "Tabasco"],
            ["México", "Monterrey", "Puebla"],
            ["Tropical", "Templado", "Húmedo"],
            ["Lago de Pátzcuaro", "Lago de Texcoco", "Lago de Cuitzeo"],
            ["Oaxaca", "Veracruz", "Tabasco"],
            ["Océano Pacífico", "Mar Caribe", "Océano Atlántico"],
            ["Península de Baja California", "Península de Florida", "Península Ibérica"],
            ["Chihuahua", "Coahuila", "Baja California"],
            ["Solo Yucatán", "Tabasco y Campeche", "Veracruz y Tabasco"],
            ["Iztaccíhuatl", "Nevado de Toluca", "La Malinche"],
            ["Quintana Roo", "Tabasco", "Chiapas"],

            # Ciencia
            ["Respiración de las plantas", "Reproducción vegetal", "Crecimiento de las plantas"],
            ["Solo sólido y líquido", "Cuatro estados", "Cinco estados"],
            ["Solo los planetas", "Las estrellas del universo", "La Vía Láctea"],
            ["Músculos del cuerpo", "Órganos internos", "Tejido nervioso"],
            ["Glóbulos blancos", "Plaquetas", "Células madre"],
            ["Solo la lluvia", "Solo la evaporación", "Solo los ríos"],
            ["Solo animales", "Solo plantas", "Solo el clima"],
            ["Pensar", "Respirar", "Digerir alimentos"],
            ["Solo los herbívoros", "Solo los carnívoros", "Solo las plantas"],
            ["Montañas", "Volcanes", "Océanos"],
            ["Magnetismo", "Electricidad", "Energía solar"],
            ["Solo superficie", "Cuatro capas", "Cinco capas"],
            ["El hígado", "El corazón", "El cerebro"],
            ["Dióxido de carbono", "Nitrógeno", "Hidrógeno"],

            # Cultura Popular
            ["Un político", "Un deportista", "Un científico"],
            ["Una fiesta de cumpleaños", "Un carnaval", "Una feria"],
            ["Las tortas", "Las quesadillas", "Los tamales"],
            ["Juguetes modernos", "Dulces típicos", "Instrumentos musicales"],
            ["Una comida típica", "Un baile", "Una artesanía"],
            ["Un tipo de comida", "Un juego tradicional", "Un traje típico"],
            ["El béisbol", "El básquetbol", "El tenis"],
            ["Juguetes electrónicos", "Decoraciones navideñas", "Máscaras festivas"],
            ["Una comida", "Una canción", "Una artesanía"],
            ["Un platillo típico", "Un instrumento musical", "Un traje tradicional"],
            ["Españoles", "Franceses", "Portugueses"],
            ["Un códice azteca", "Un libro colonial", "Un texto moderno"],
            ["Un ritual para pedir buena cosecha", "Un festival religioso", "Una celebración de nacimiento"],
            ["Animal sagrado", "Guardián del sol", "Especie de ave"]
        ]
        self.resultado = None   
        

    def seleccionar_pregunta(self):
        indice = random.randint(0, len(self.preguntas) - 1)
        self.pregunta_actual = self.preguntas[indice]
        self.correcta = self.respuestas_correctas[indice]
        self.incorrectas = random.sample(self.respuestas_incorrectas[indice], 2)
        self.mostrar_pregunta()

    def mostrar_pregunta(self):
        self.ventana = tk.Tk()
        self.ventana.geometry("400x400")
        self.ventana.title("Preguntas de Aventura")

        self.label_pregunta = tk.Label(self.ventana, text=self.pregunta_actual, wraplength=400)
        self.label_pregunta.pack(pady=20)

        self.opciones = [self.correcta] + self.incorrectas
        random.shuffle(self.opciones)

        self.botones = []
        for respuesta in self.opciones:
            boton = tk.Button(self.ventana, text=respuesta, command=lambda r=respuesta: self.verificar_respuesta(r))
            boton.pack(pady=5)
            self.botones.append(boton)

        self.label_resultado = tk.Label(self.ventana, text="", fg="red")
        self.label_resultado.pack(pady=20)

        self.ventana.mainloop()


        

    def verificar_respuesta(self, respuesta):
        if respuesta == self.correcta:
            self.label_resultado.config(text="¡Correcto!", fg="green")
            self.resultado = True
        else:
            self.label_resultado.config(text="¡Incorrecto!", fg="red")
            self.resultado = False

        for boton in self.botones:
            boton.config(state=tk.DISABLED)

        # Cerrar la ventana después de un breve retraso
        self.ventana.after(2000, self.ventana.destroy)

    def obtener_resultado(self):
        return self.resultado

