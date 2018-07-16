# if - else

print("Verificación de acceso")

edadUsuario = int(input("Introduce tu edad, por favor: "))

if edadUsuario < 18:
    print("No puedes pasar")
elif edadUsuario > 100: # elif = else if
    print("Edad incorrecta")
else:
    print("Puedes pasar")

print("El programa ha finalizado")

# Evaluación nota

print("Verificación de calificación")

notaAlumno = int(input("Introduce tu nota, por favor: "))

if notaAlumno < 5:
    print("Insuficiente")
elif notaAlumno < 6: 
    print("Suficiente")
elif notaAlumno < 7:
    print("Bien")
elif notaAlumno < 8:
    print("Notable")
elif notaAlumno < 9:
    print("Excelente")
else:
    print("Sobresaliente")

print("El programa ha finalizado")