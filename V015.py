# Bucle for (Recorriendo strings, tipo range, notaciones especiales con print)

for i in ['Pildoras', 'Informáticas', 8]:
    print("Hola", end=" ") # Argumento 'end' para que no haga un salto de linea y haga espacio

print() # Dividiendo String

print('Imprimiendo la misma cantidad de veces como letras que tenga la palabra')
for i in 'google@gmail.com':
    print(i, end=" ")

print() # Evaluando correo electrónico

contador = 0

miEmail = input('Introduce tu dirección de email: ')

for i in miEmail:
    if i == '@' or i == '.':
        contador = contador + 1

if email: # if email == True:
    print('El email es correcto') # Porque tiene una '@'
else:
    print('El email es incorrecto')
