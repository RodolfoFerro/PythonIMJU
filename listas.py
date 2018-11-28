# Autor: Rodolfo Ferro
# Contacto: ferro@cimat.mx

# Creamos una lista:
sexto_economico = ["Guadalupe", "Sara", "Isaias"]
# print(type(sexto_economico))
# print(sexto_economico[1])

abc = ["a", "b", "c", "d",
       "e", "f", "g", "h",
       "i", "j", "k", "l"]

# _len_ indica la longitud de la lista,
# esto es, cuantos elementos tiene.
print("La logintud de tu abecedario es:", len(abc))

# Los dos puntos : (slicing) indican el acceso a
# elementos contenidos entre el indice inicial
# y el indice final.
print(abc[5:11])

# _range_ es una funcion que crea una lista con
# elementos en el rango especificado.
print(list(range(5, 11)))
