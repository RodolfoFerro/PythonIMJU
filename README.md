# Programando videojuegos con Python


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
