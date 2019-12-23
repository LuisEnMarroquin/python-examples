# Una 'lista' en Python es como un 'Array' en Java
# En Python las listas se pueden expandir dinámicamente

nombreLista = ["Texto", 100]
print(nombreLista) # Imprimiendo la lista

nombres = ["María", "Pepe", "Juan", "Antonio"]
print(nombres[:])

print(nombres[2]) # Accedendo a un indice dentro de la lista
print(nombres[-2]) # Un indice negativo indica que se comenzará a contar la lista de atras hacia adelante, ya no comenzando en el 0, si no en el 1

print(nombres[0:3]) # Accediendo solo a una porción de la lista: Los indices 0, 1 y 2
print(nombres[:3]) # Lo mismo que la linea de arriba

print(nombres[2:]) # Accediendo desde el elemento que tiene el indice 2 hasta el final

nombres.append("Sandra") # Agregando elemento al final de la lista

nombres.insert(2, "Sofia") # Agregando en un lugar en concreto de la lista

nombres.extend(["Luis", "Ana", "Manuel"]) # Agregando muchos elementos a la lista

print(nombres)

indice = nombres.index('Antonio') # Devolviendo el indice de un elemento
print(indice)

# En las listas si se pueden repetir elementos

print("Pepe" in nombres) # Checando si "Pepe" existe en la lista

miLista = ["María", 5, True, 78.35] # En Python las listas pueden guardar diferentes tipos de valores

print(miLista[1]) # Imprimiendo elemento de la lista

miLista.remove(5) # Eliminando elemento de la lista

print(miLista[:]) # Imprimiendo la lista completa

miLista.pop() # Eliminando el ultimo elemento de una lista

print(miLista) # Imprimiendo la lista completa

lista1 = ["María", 5, True, 78.35]
lista2 = ["Catarina", "Lucía"]

lista3 = lista1 + lista2 # Concatenando listas
print(lista3[:])

lista4 = [1,2,3] * 3 # Pondrá 3 veces la lista
print(lista4) 
