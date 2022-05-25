from Palabras import palabras
import random

def Ahorcado():
    print("======================\n")
    print("Bienvenido (a) al juego del Ahorcado.!\n")
    print("======================\n")   
    
    palabra= Obtener_palabra_valida(palabras)

def Obtener_palabra_valida(l_palabras):
    # Seleccionar una palabra al azar de la lista.
    palabra= random.choice(palabras)
    return palabra.upper()

#https://www.youtube.com/watch?v=tWnyBD2src0&ab_channel=freeCodeCampEspa%C3%B1ol
#Seguir!