import math

def evalAge(age):
  if age < 0:
    raise TypeError('Negative ages are not allowed') # raise + exceptionType
  if age < 20:
    return 'You are very young'
  if age < 40:
    return 'You are young'
  if age < 65:
    return 'You are not young'
  if age < 100:
    return 'You are clever'
  return 'You are over 100 years'

print(evalAge(18))

def calculaRaiz(num1):
  if num1 < 0:
    raise ValueError('El número no puede ser négativo')
  else:
    return math.sqrt(num1)

op1 = (int(input('Introduce un número: ')))

try:
  print(calculaRaiz(op1))
except ValueError as ErrorDeNumeroNegativo:
  print(ErrorDeNumeroNegativo)

print('Programa terminado')
