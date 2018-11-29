# Autor: Rodolfo Ferro
# Contacto: ferro@cimat.mx

from time import sleep

# segundos = 5
# print("Incia el conteo...")
# sleep(segundos)
# print("Woow, han pasado", segundos, "segundos.")

# Funcion para limpiar la pantalla:
def limpiar(saltos):
    linea = "\n" * saltos
    print(linea)
    return

# Saludo:
print("Hola a todos!")
print("Les voy a contar unos chistes!")
print()
sleep(2)
limpiar(1000)

# Chiste 1:
print("– No cabia duda...", end='')
input()
print("– Y duda se fue en otro coche...")
print("BA-DUM-TSS!")
print()
sleep(3)
limpiar(1000)

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
limpiar(1000)

# Chiste 3:
print("– Te puedo robar un beso?", end='')
input()
print("– Con esa cara, mejor robame el celular...")
print("BA-DUM-TSS!")
print()
sleep(3)
limpiar(1000)

# Chiste 4:
print("– Amor, te gusta mi disfraz?", end='')
input()
print("– Si amor, te ves bonita de vaca.", end='')
input()
print("– PERO SOY UN DALMATA!")
print("BA-DUM-TSS!")
print()
sleep(2)
limpiar(1000)

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
