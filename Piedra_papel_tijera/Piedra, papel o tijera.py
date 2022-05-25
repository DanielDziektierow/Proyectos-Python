import random
import string as str

def Jugar():
    Opcion_pc= random.randint(1,3)

    Opcion_usuario= input("Escriba una opcion:\n1. Piedra.\n2. Papel.\n3. Tijera.\n")
    if(Opcion_usuario == "1" or Opcion_usuario.upper() == "PIEDRA"):
        if(Opcion_pc == 1):
            print("Empate, juguemos otra!\n")
        elif(Opcion_pc == 2):
            print("Gane >:)\n")
        elif(Opcion_pc == 3):
            print("Ganaste :'(\n")
        else:
            print("Error de sistema.\n")
    
    elif(Opcion_usuario == "2" or Opcion_usuario.upper() == "PAPEL"):
        if(Opcion_pc == 2):
            print("Empate, juguemos otra!\n")
        elif(Opcion_pc == 3):
            print("Gane >:)\n")
        elif(Opcion_pc == 1):
            print("Ganaste :'(\n")
        else:
            print("Error de sistema.\n")
    
    elif(Opcion_usuario == "3" or Opcion_usuario.upper() == "TIJERA"):
        if(Opcion_pc == 3):
            print("Empate, juguemos otra!\n")
        elif(Opcion_pc == 1):
            print("Gane >:)\n")
        elif(Opcion_pc == 2):
            print("Ganaste :'(\n")
        else:
            print("Error de sistema.\n")
    
    else:
        print("Error de sistema.\n")

Jugar()
