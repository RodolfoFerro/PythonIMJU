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
