# Autor: Rodolfo Ferro
# Descripcion: Juego de adivinar el numero

# 1. Importar random.randint
# 2. Iniciamos el no. de intentos en 0
# 3. Saludamos al usuario
# 4. Generamos no. aleatorio
# 5. La maquina responde e inicia el juego
# 6. Usuario intenta adivinar.
#   A. Input de intento.
#   B. Convertimos a entero.
#   C. Comparamos no. con intento.

from random import randint

no_intentos = 0

usuario = input("Escribe tu nombre: ")
print("Que onditrix, " + usuario + ".")

numero = randint(1, 20)
print("He pensado en un numero entre 1 y 20...")


for i in range(5):
    mi_intento = input("Escribe tu intento: ")
    mi_intento = int(mi_intento)
    no_intentos = no_intentos + 1

    if mi_intento > numero:
        print("El numero que he pensado es mas pequeño. Intenta de nuevo.")
    elif mi_intento < numero:
        print("El numero que he pensado es mas grande. Intenta de nuevo.")
    else:
        print("Adivinaste en", no_intentos, "intentos.")
        print("El numero que he pensado es:", numero)
        break

if no_intentos >= 5:
    print("Suerte para la siguiente, el numero era:", numero)
