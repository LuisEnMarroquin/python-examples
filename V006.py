# Creando y llamando a una función

def suma():
    num1 = 5
    num2 = 7
    print(num1 + num2)

suma()

# Paso de parámetros

num1 = 5
num2 = 7

def sumaParams(num1, num2):
    print(num1 + num2)

sumaParams(num1, num2)

sumaParams(50, 20)

# Función que devuelve algo: 'return'

def sumaReturn(num1, num2):
    resultado = num1 + num2
    return resultado

print(sumaReturn(20, 80))

almacenaResult = sumaReturn(10,40)
print(almacenaResult)
