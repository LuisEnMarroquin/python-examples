# Excepciones varias y finally

def suma(num1, num2):
	return num1+num2

def resta(num1, num2):
	return num1-num2

def multiplica(num1, num2):
	return num1*num2

def divide(num1,num2):
    try:		
	    return num1/num2
    except ZeroDivisionError:
        print('No se puede dividir entre 0')
        return "Operación erronea"

while True:
	try:
		op1=(int(input("Introduce el primer número: ")))
		op2=(int(input("Introduce el segundo número: ")))
		break # Leave the while
	except ValueError: 
		print('Los valores introducidos no son correctos. Intentalo otra vez')

operacion=input("Introduce la operación a realizar (suma,resta,multiplica,divide): ")

if operacion=="suma":
	print(suma(op1,op2))

elif operacion=="resta":
	print(resta(op1,op2))

elif operacion=="multiplica":
	print(multiplica(op1,op2))

elif operacion=="divide":
	print(divide(op1,op2))

else:
	print ("Operación no contemplada")

print("Operación ejecutada. Continuación de ejecución del programa ")

#####

def dividir():

    try:
        op1=(float(input("Introduce el primer número: ")))
        op2=(float(input("Introduce el segundo número: ")))
        print('La división es: ' + str(op1/op2))
    except ValueError:
        print('El valor introducido es erroneo')
    except ZeroDivisionError:
        print('No se puede dividir entre 0')
    except: # Captura cualquier tipo de excepción
        print('Ha ocurrido un error')
    finally:
        print('Calculo finalizado')

    # Si el try no tiene 'except' pero si tiene 'finally' el programa caerá hasta haber ejecutado el finally

dividir()
