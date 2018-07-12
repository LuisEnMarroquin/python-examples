# Tuplas
# Las tuplas son listas inmutables, es decir no son modificables después de su creación

# Desventajas:
    # No se permiten añadir, eliminar o mover elementos (NO -> append, extend, remove)
    # Si permiten extraer porciones, aunque el resultado de la extracción es una tupla nueva
    # No permiten búsquedas (no index)

# Ventajas:
    # Las tuplas son más rapidas
    # Ocupan menos espacio en memoria
    # Formatean Strings
    # Pueden usarse como claves en un diccionaria (las listas no)
    # Si permiten comprobar si un elemento se encuentra en una tupla

nombreLista = (1,2,3) # Tupla (lleva parentesis en vez de corchetes)
nombreTupla = 1,2,3 # Tupla (puede no llevar parentesis, aunque es recomendable ponerselos)

miTupla = ("Juan", 13, 1, 1995) 
print(miTupla[2]) # Imprimiendo elemento en la posición 2 de la tupla

# Creando una lista apartir de una tupla
miLista = list(miTupla)
print(miLista) # Imprimiendo la lista (se puede saber que es una lista porque tiene corchetes)

# Creando una tupla apartir de una lista
Tupla = tuple(miLista)
print(Tupla) # Imprimiendo la tupla (se puede saber que es una tupla porque tiene parentesis)

# 11:50
