#Piedra gana a tijera (pi>ti).
#Papel gana a piedra (pa>pi).
#Tijera gana a papel (ti>pa).
import random

def Jugar():
    usuario= input("Escoge una opcion: 'pi', 'pa' o 'ti'\n").lower()

    pc= random.choice(['pi', 'pa', 'ti'])

    if(usuario == pc):
        return "Empate!\n"

    if gano_el_jugador(usuario, pc):
        return "Ganaste.\n"
    return "Perdiste.\n"

def gano_el_jugador(jugador, oponente):
    #Retornar True si gana el jugador.
    if((jugador == 'pi' and oponente == 'ti') or (jugador== 'pa' and oponente== 'pi') or (jugador== 'ti' and oponente== 'pa')):
        return True
    else:
        return False

print(Jugar())