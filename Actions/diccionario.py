import tkinter as tk
from tkinter import messagebox
from tkinter import PhotoImage
from PIL import Image, ImageTk
import random


datos = {"(La Pirámide de Kukulkán en Chichén Itzá, funciona como un calendario solar" : "Imagenes/maya.jpg", 
         "Machu Picchu, fue una ciudad inca, refleja los profundos conocimientos astronómicos de los incas" : "Imagenes/inca.jpg",
         "Las pirámides de Giza, son las más antiguas y grandes de las tres pirámides de Egipto" : "Imagenes/egipcia.jpg",
         "El Coliseo de Roma, es un anfiteatro de la época del Imperio romano" : "Imagenes/roma.jpg",
         "El partenón de Atenas, es un templo dedicado a la diosa Atenea" : "Imagenes/griega.jpg",
         "La Gran Muralla China, es una antigua fortificación china construida para proteger la frontera norte del imperio chino" : "Imagenes/china.jpg",
         "Los geo-glifos de Nazca, son antiguos dibujos en la tierra que se encuentran en la Pampa de Nazca, en Perú" : "Imagenes/nazca.jpg",
         "Los Atlantes de Tula, son esculturas de guerreros toltecas" : "Imagenes/tolteca.jpg",
         "El Templo de Kalasa, es un templo hindú en la India" : "Imagenes/india.jpg",
         "El Templo Mayor de Tenochtitlán, es un templo azteca que reflejaba la relación entre el cielo, la tierra y el inframundo" : "Imagenes/azteca.jpg"}


def ventana_diccionario():
    #Selecciona un elemento aleatorio del diccionario
    texto, ruta_imagen = random.choice(list(datos.items())) 

    #crear ventana
    ventana = tk.Tk()
    ventana.title("Datazos de Maravillas")

    #Mostrar texto
    etiqueta_texto = tk.Label(ventana, text=texto, font=("Arial", 12),wraplength=400)
    etiqueta_texto.pack(pady=10)

     # Cargar y mostrar imagen usando Pillow
    imagen_original = Image.open(ruta_imagen)  # Abrir imagen
    imagen_resized = imagen_original.resize((400, 300))  # Ajustar tamaño si es necesario
    imagen = ImageTk.PhotoImage(imagen_resized)
    etiqueta_imagen = tk.Label(ventana, image=imagen)
    etiqueta_imagen.image = imagen  # Evitar que se elimine de memoria
    etiqueta_imagen.pack()

    
   
    ventana.after(5000, ventana.destroy)  # Cerrar ventana después de 5 segundos
    ventana.mainloop()

ventana_diccionario()

         