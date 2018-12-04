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
