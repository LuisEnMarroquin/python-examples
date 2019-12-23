# Diccionarios: Asociaciones = Clave - Valor

# Creando un diccionario
miDiccionario = {"Alemania":"Berlín", "Francia":"París", "Reino Unido":"Londres", "España":"Madrid"}

# Imprimiendo todo el diccionario
print(miDiccionario)

# Imprimiendo elemento en especifico del diccionario
print(miDiccionario["Francia"])

# Agregando entrada al diccionario
miDiccionario["Italia"]="Lisboa"
# Corrigiendo entrada del diccionario
miDiccionario["Italia"]="Roma"

# Imprimiendo todo el diccionario
print(miDiccionario)

# Eliminando un elemento del diccionario
del miDiccionario["Reino Unido"]

# Imprimiendo todo el diccionario
print(miDiccionario)

# Creando diccionario con varios tipos de datos
diccion = {"Alemania":"Berlín", 23:"Jordan", "Mosqueteros":3}

# Imprimiendo todo el diccionario
print(diccion)

# Creando tupla
miTupla = ["España", "Francia", "Reino Unido", "Alemania"]

# Creando diccionario apartir de una tupla
diccionario = { miTupla[0]:"Madrid", miTupla[1]:"París", miTupla[2]:"Londres", miTupla[3]:"Berlín" }

# Imprimiendo todo el diccionario
print(diccionario)

# Creando diccionario que almacenará una tupla
myDiccionary = { 23:"Jordan", "Nombre":"Michael", "Equipo":"Chicago", "Anillos":[1991,1992,1993,1996,1997,1998] }

# Imprimiendo todo el diccionario
print(myDiccionary)

# Accediendo a elemento en especifico del diccionario
print(myDiccionary["Equipo"])

# Accediendo a la tupla dentro del diccionario
print(myDiccionary["Anillos"])

# Creando diccionario que almacenará otro diccionario
diccionarioEnDiccionario = { 23:"Jordan", "Nombre":"Michael", "Equipo":"Chicago", "Anillos":{"temporadas":[1991,1992,1993,1996,1997,1998]} }

# Accediendo al diccionario dentro de otro diccionario que dentro tiene una tupla
print(diccionarioEnDiccionario["Anillos"])

# Imprimiendo los datos antes del :
print(diccionarioEnDiccionario.keys())

# Imprimiendo los datos después del :
print(diccionarioEnDiccionario.values())

# Imprimiendo la longitud del diccionario
print(len(diccionarioEnDiccionario))
