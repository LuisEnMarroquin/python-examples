# Generadores

def generaParesF(limite): # Función
    num = 1
    miLista = []
    while num<limite:
        miLista.append(num*2)
        num = num + 1
    return miLista
print(generaParesF(5))

def generaParesG(limite): # Generador
    num = 1
    while num<limite:
        yield num*2 # 'yield' construye un objeto iterable donde va almacenando los números de uno en uno
        num = num + 1
devuelvePares = generaParesG(5)

# for i in devuelvePares:
#     print(i)

print(next(devuelvePares))
print('Aquí podria ir mas código')
print(next(devuelvePares))
print('Aquí podria ir mas código')
print(next(devuelvePares))

# Hasta aquí el generador solo ha generado hasta el número 6 y no generará lo demás hasta que se use otra vez la funcion next
