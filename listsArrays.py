# list == array # https://www.w3schools.com/python/python_arrays.asp

print('Print list:', ['Text', 100, True, 78.35])

listNames = ['Mary', 'Luke', 'John', 'Paul']

print('Print list:', listNames[:])

print('Looking index:', listNames[2])

print('Reverse index:', listNames[-2])

print('Sublist:', listNames[0:2])

print('Sublist:', listNames[:2])

print('Sublist:', listNames[2:])

listNames.append('Sandra')

print('Print list:', listNames)

listNames.insert(2, 'Donald')

print('Print list:', listNames)

listNames.extend(['Abigail', 'Beatrix'])

print('Print list:', listNames)

print('Index of Luke:', listNames.index('Luke'))

print('Is Pepe in list:', 'Pepe' in listNames)

listNames.remove('John')

print('Print list:', listNames)

listNames.pop()

print('Print list:', listNames)

listNumbers = [1, 2, 3] * 3

print('Multiply list:', listNumbers)
