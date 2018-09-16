# Generadores: yield form (como for anidado)

def devuelve_ciudades(*ciudades): # El asterisco significa que recibirá cualquier número de ciudades en forma de tupla
    for elemento in ciudades:
        yield elemento
        # for subElemento in elemento:
        #     yield subElemento
        yield from elemento

ciudades_devueltas = devuelve_ciudades("Madrid", "Barcelona", "Belgica", "París")

print(next(ciudades_devueltas))

print(next(ciudades_devueltas))
print(next(ciudades_devueltas))
print(next(ciudades_devueltas))
print(next(ciudades_devueltas))
print(next(ciudades_devueltas))
print(next(ciudades_devueltas))

print(next(ciudades_devueltas))

print(next(ciudades_devueltas))
print(next(ciudades_devueltas))
print(next(ciudades_devueltas))
print(next(ciudades_devueltas))
print(next(ciudades_devueltas))
print(next(ciudades_devueltas))
print(next(ciudades_devueltas))
print(next(ciudades_devueltas))
print(next(ciudades_devueltas))