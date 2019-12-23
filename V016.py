# Range

for i in range(5): # Imprimira números del 0 al 4
    print(f"Valor de la variable {i}") # Función de tipo f (para sumar textos con variables)

for i in range(5, 10):
    print(i)

for i in range(5, 50, 3):
    print(i)

# Evaluando email

valido = False

email = input("Introduce tu email: ")

for i in range(len(email)):
    if email[i] == '@':
        valido = True

if valido: 
    print("Email correcto")
else: 
    print("Email incorrecto")





#