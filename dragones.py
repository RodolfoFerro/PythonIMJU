# Autor: Rodolfo Ferro
# Juego: Dragon's realm

# 1. Importamos random, time
# 2. Crear funcion de Intro
# 3. Crear funcion escoge_cueva
# 4. Crear funcion verifica_cueva
#   a. Crear suspenso
#   b. Generar numero aleatorio (1, 2)
#   c. Comparar si ganamos
# 5. Preguntar si queremos jugar de nuevo

from random import randint
from time import sleep


def intro():
    texto = """Estas en una tierra llena de dragones.
Frente a ti, ves dos cuevas. En una cueva el dragon es
amistoso y te va a compartir su tesoro. El otro dragon
es codicioso y hambriento y te va a comer sin chistar..."""
    print(texto)
    print()
    return


def escoge_cueva():
    cueva = ""
    while cueva != "1" or cueva != "2":
        cueva = input("Escoge una cueva (1/2): ")
    return cueva


intro()
cueva = escoge_cueva()
