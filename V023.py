# Lanzar excepciones

def evaluaEdad(edad):

    if edad < 0:
        raise TypeError("No se permiten edades negativas") # raise + tipo de excepción

    if edad < 20:
        return "Eres muy joven"
    elif edad < 40:
        return "Eres joven"
    elif edad < 65:
        return "No eres joven"
    elif edad < 100:
        return "Cuídate..."

print(evaluaEdad(18))

##############################

import math

def calculaRaiz(num1):
    if num1 < 0:
        raise ValueError("El número no puede ser négativo")
    else:
        return math.sqrt(num1)

op1 = (int(input('Introduce un número: ')))

try:
    print(calculaRaiz(op1))
except ValueError as ErrorDeNumeroNegativo:
    print(ErrorDeNumeroNegativo)

print('Programa terminado')
