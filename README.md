# Programando videojuegos con Python

## Códigos del curso

Código `saludo.py`:

```python
# Autor: Rodolfo Ferro
# Contacto: ferro@cimat.mx

# Pido el nombre:
nombre = input("Escribe tu nombre: ")
print("Mucho gusto,", nombre)

# Pido la edad:
edad = input("Escribe tu edad: ")
edad = int(edad)

# Comparo la edad:
if edad >= 18 and edad <= 60:
    print("Es legal.")
elif edad > 0 and edad < 18:
    print("Wiu, wiu, wiu.")
else:
    print("No hay, no existe.")
```

Código `listas.py`:
```python
# Autor: Rodolfo Ferro
# Contacto: ferro@cimat.mx

# Creamos una lista:
sexto_economico = ["Guadalupe", "Sara", "Isaias"]
# print(type(sexto_economico))
# print(sexto_economico[1])

abc = ["a", "b", "c", "d", \
       "e", "f", "g", "h", \
       "i", "j", "k", "l"]

# _len_ indica la longitud de la lista,
# esto es, cuantos elementos tiene.
print("La logintud de tu abecedario es:", len(abc) )

# Los dos puntos : (slicing) indican el acceso a
# elementos contenidos entre el indice inicial
# y el indice final.
print( abc[5:11] )

# _range_ es una funcion que crea una lista con
# elementos en el rango especificado.
print( list( range(5, 11) ) )
```

Código `alumnos.py`:
```python
from random import randint

alumnos = ["Guadalupe", "Sara", "Isaias", "Saulo", "Gabriel", "Chava"]
print(alumnos)

for index, alumno in enumerate(alumnos):
    alumnos[index] = [alumno, randint(5, 10)]

print(alumnos)

for alumno in alumnos:
    print("El alumno {} tiene calificacion {}.".format(alumno[0], alumno[1]))
```

Código `adivina adivinador.py`, juego de adivinar el número:
```python
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

```

Código `chistes.py`:
```python
# Autor: Rodolfo Ferro
# Contacto: ferro@cimat.mx

from time import sleep

# segundos = 5
# print("Incia el conteo...")
# sleep(segundos)
# print("Woow, han pasado", segundos, "segundos.")

# Saludo:
print("Hola a todos!")
print("Les voy a contar unos chistes!")
print()
sleep(2)

# Chiste 1:
print("– No cabia duda...", end='')
input()
print("– Y duda se fue en otro coche...")
print("BA-DUM-TSS!")
print()
sleep(3)

# Chiste 2:
print("– A que te dedicas?", end='')
input()
print("– A mover vacas...", end='')
input()
print("– Eres ganadero?", end='')
input()
print("– No, soy maestro de zumba. xdxdxd")
print("BA-DUM-TSS!")
print()
sleep(3)

# Chiste 3:
print("– Te puedo robar un beso?", end='')
input()
print("– Con esa cara, mejor robame el celular...")
print("BA-DUM-TSS!")
print()
sleep(3)

# Chiste 4:
print("– Amor, te gusta mi disfraz?", end='')
input()
print("– Si amor, te ves bonita de vaca.", end='')
input()
print("– PERO SOY UN DALMATA!")
print("BA-DUM-TSS!")
print()
sleep(2)

# Despedida:
print("Espero te hayas divertido.")
print("Doy clases los jueves, no cobro mucho. xdxdxd")

fin = """  _________________________________
 |.--------_--_------------_--__--.|
 ||    /\ |_)|_)|   /\ | |(_ |_   ||
 ;;`,_/``\|__|__|__/``\|_| _)|__ ,:|
((_(-,-----------.-.----------.-.)`)
 \__ )        ,'     `.        \ _/
 :  :        |_________|       :  :
 |-'|       ,'-.-.--.-.`.      |`-|
 |_.|      (( (*  )(*  )))     |._|
 |  |       `.-`-'--`-'.'      |  |
 |-'|        | ,-.-.-. |       |._|
 |  |        |(|-|-|-|)|       |  |
 :,':        |_`-'-'-'_|       ;`.;
  \  \     ,'           `.    /._/
   \/ `._ /_______________\_,'  /
    \  / :   ___________   : \,'
     `.| |  |           |  |,'
       `.|  |           |  |
         |  | SSt       |  |"""
print(fin)

```

Archivo `dragones.py`:
```python
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
    while cueva != "1" and cueva != "2":
        cueva = input("Escoge una cueva (1/2): ")
    return cueva


def verifica_cueva(cueva):
    # Suspenso:
    print("Te acercas a la cueva...")
    sleep(2)
    print("Esta oscuro y tenebroso...")
    sleep(2)
    print("Un enorme dragon salta frente a ti! Abre su boca y...")
    sleep(2)

    dragon = randint(1, 2)

    if dragon == int(cueva):
        print("EL DRAGON TE HA ENTREGADO SU TESORO!")
    else:
        print("EL DRAGON TE HA COMIDO, POR FEO.")


restart = "si"
while restart == "si" or restart == "s":
    intro()
    cueva = escoge_cueva()
    verifica_cueva(cueva)

    restart = input("Deseas jugar de nuevo? (si/no): ")
    print()

```

Archivo `conversiones.py`:
```python
def metros_a_centimetros(valor):
    resultado = 100 * valor
    return resultado


def centimetros_a_metros(valor):
    resultado = valor / 100
    return resultado


def celsius_a_kelvin(valor):
    resultado = valor + 273.15
    return resultado


def celsius_a_fahrenheit(valor):
    resultado = (9 / 5) * valor + 32
    return resultado


celsius = input("Introduce º Celsius: ")
celsius = float(celsius)
fahrenheit = celsius_a_fahrenheit(celsius)
print(fahrenheit, "ºF")

```
