from Palabras import palabras
from ahorcado_diagramas import vidas_diccionario_visual

import random
import string

def Ahorcado():
    print("======================\n")
    print("Bienvenido (a) al juego del Ahorcado.!\n")
    print("======================\n")   
    
    palabra= Obtener_palabra_valida(palabras)
    letras_adivinar= set(palabra)
    letras_adivinadas= set()
    abecedario= set(string.ascii_uppercase)
    vidas= 7

    while len(letras_adivinar) > 0 and vidas > 0:
        print(f"Te quedan {vidas} vidas y has usado estas letras: {' '.join(letras_adivinadas)}")

        #mostrar estado actual de la palabra
        palabra_lista = [letra if letra in letras_adivinadas
        else '-' for letra in palabra]
        #Mostrar estado del ahorcado
        print(vidas_diccionario_visual[vidas])
        #Mostrar letras separadas por un espacio.
        print(f"Palabra: {' '.join(palabra_lista)}")

        letra_usuario= input("Escoge una letra: ").upper()
        # Si la letra escogida por el usuario esta en el abecedario
        # y no esta en el conjunto de letras que ya se han ingresado
        # se anade la letra al conjunto de letras ingresadas.
        if letra_usuario in abecedario - letras_adivinadas:
            letras_adivinadas.add(letra_usuario)

            #Si la letra esta en la palabra
            # quitar  la letra del conjunto de letras 
            # pendientes por adivinar.
            # Si no esta en la palabra, quitar una vida.
            if letra_usuario in letras_adivinar:
                letras_adivinar.remove(letra_usuario)
                print('') 
            else:
                vidas = vidas - 1
                print(f"\nTu letra {letra_usuario}, no esta en la palabra.")
        # Si la letra escogida por el usuario, ya fue ingresada
        elif letra_usuario in letras_adivinadas:
            print("\nYa escogiste esa letra, escoge una nueva.")
        else:
            print("\nEsta letra, no es valida.")
    # Eljuego llega a esta linea cuando se adivinan todas las letras de la palabra
    # o cuando se agotan las vidas del jhugador.
    if vidas == 0:
        print(vidas_diccionario_visual[vidas])
        print(f"Ahorcado!! Perdiste. Lo lamento mucho. La palabra era: {palabra}")
    else:
        print(f"Excelente! adivinaste la palabra {palabra}!")

def Obtener_palabra_valida(l_palabras):
    # Seleccionar una palabra al azar de la lista.
    palabra= random.choice(palabras)
    while '-' in palabra or ' ' in palabra:
        palabra= random.choice(palabras)
    return palabra.upper()

Ahorcado()