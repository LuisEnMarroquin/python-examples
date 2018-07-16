# Operadores lógicos 'and' y 'or' y el operador 'in'

print("Programa de Becas 2018")

distanciaEscuela = int(input("Introduce la distancia en kilómetros: "))
numeroDeHermanos = int(input("Introduce el número de hermanos: "))
salarioFamiliar = int(input("Introduce el salario familiar: "))

if distanciaEscuela>40 and numeroDeHermanos>2 or salarioFamiliar<20000:
    print("Tienes derecho a beca")
else:
    print("No tienes derecho a beca")

# Operador 'in'

print("Asignaturas optativas 2018 (Programación, Software, Videojuegos)")

opcion = input("Escribe la asignatura escogida: ")

asignatura = opcion.lower() # Convirtiendo el input a minúsculas

if asignatura in ('programación', 'software', 'videojuegos'):
    print("Asignatura elegida " + asignatura)
else:
    print("La asignatura escogida no está contemplada")


#