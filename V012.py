# Concatenación de operadores de comparación

edad = 77

if 0 < edad < 100: # La edad tiene que ser de entre 1 a 99 años
    print("La edad es correcta")
else:
    print("La edad es incorrecta")

# Evaluando el salario

salarioPresidente = int(input("Introduce el salario del presidente: "))
print("El salario del presidente es: " + str(salarioPresidente)) # Python no permite la concatenación de diferentes tipos de datos

salarioDirector = int(input("Introduce el salario del director: "))
print("El salario del director es: " + str(salarioDirector))

salarioJefeArea = int(input("Introduce el salario del jefe de area: "))
print("El salario del jefe de area es: " + str(salarioJefeArea))

salarioAdministrativo = int(input("Introduce el salario del administrativo: "))
print("El salario del administrativo es: " + str(salarioAdministrativo))

if salarioAdministrativo < salarioJefeArea < salarioDirector < salarioPresidente: 
    print("Todo funciona correctamente")
else:
    print("Hay un error con los salarios")
