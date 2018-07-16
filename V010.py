# Condicional IF

def evaluacion(nota):
    valoracion = 'aprovado'
    if nota < 5:
        valoracion = 'reprobado'
    return valoracion

print(evaluacion(4))

# Input por teclado

print("Programa de evaluación de notas de alumnos")

notaAlumno = input("Introduce la nota del alumno: ") # Lo que se introduzca será considerado como texto

def evaluacion2(nota):
    valoracion = 'aprovado'
    if nota < 5:
        valoracion = 'reprobado'
    return valoracion

print(evaluacion2(int(notaAlumno)) # Casting del texto a entero