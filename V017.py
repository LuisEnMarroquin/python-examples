# Bucle while

i = 1
while i<=10:
    print("Ejecución: " + str(i))
    i = i + 1
print('Terminó la ejecución')

# Evaluando edad

edad = int(input("Introduce tu edad, por favor: "))

while edad<=0 or edad>100:
    print('Has introducido una edad negativa o una edad mayor a 100')
    edad = input("Introduce tu edad, por favor: ")

print('Tu edad es de ' + str(edad) + " años.")

# Evitando que un bucle sea infinito e importando paquetes

import math # Importando math

print('Programa de calculo de raíz cuadrada')

numero = int(input('Introduce un número, por favor: '))

intentos = 0

while numero<0: # Bucle while indeteminado porque no se sabe si se va a ejecutar 0, 1 o 2 veces
    
    print('No se puede hallar la raíz de un número negativo')

    if intentos == 2:
        print('Has consumido demasiados intentos')
        break

    numero = int(input('Introduce un número, por favor: '))

    if numero < 0:
        intentos = intentos + 1

if intentos < 2:
    solucion = math.sqrt(numero)
    print(f"La raíz cuadrada de {numero} es {solucion}")
