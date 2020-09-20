# Bucles: Continue, pass and else

## CONTINUE

for letra in "Python":
  if letra == 'h':
    continue # Salta directamente a la siguiente vuelta del bucle
  print('Viendo la letra: ' + letra)

nombre = 'Pildoras Informáticas'
contador = 0
for letra in nombre:
  if letra == ' ':
    continue # Salta directamente a la siguiente vuelta del bucle
  contador += 1
print(nombre + ' tiene ' + str(contador) + ' letras.')

## PASS

# while True:
#     pass # Salir del bucle con: CTRL + C

# class MiClase:
#     pass # Para implementar más tarde

## ELSE

email = input('Introduce tu email, por favor: ')
for i in email:
  if i=='@':
    arroba = True
    break
else: # Este else no pertenece al 'if', pertenece al 'for' # Cuando el for acabe de ejecutarse se pasará directamente al else
  arroba = False
print('Tiene arroba: ' + str(arroba))
