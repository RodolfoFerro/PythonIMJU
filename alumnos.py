from random import randint

alumnos = ["Guadalupe", "Sara", "Isaias", "Saulo", "Gabriel", "Chava"]
print(alumnos)

for index, alumno in enumerate(alumnos):
    alumnos[index] = [alumno, randint(5, 10)]

print(alumnos)

for alumno in alumnos:
    print("El alumno {} tiene calificacion {}.".format(alumno[0], alumno[1]))
