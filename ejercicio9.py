def suma(n1, n2):
    suma = n1+n2
    return suma


def resta(n1, n2):
    resta = n1-n2
    return resta


def multiplicacion(n1, n2):
    multiplicacion = n1*n2
    return multiplicacion


def division(n1, n2):
    if n2 != 0:
        return n1/n2
    else:
        return "Error! No es posible la division por cero"


n1 = float(input("Ingre el primer numero: "))
n2 = float(input("Ingrese el segundo numero: "))
print("Ingrese un numero:")
print("1=suma, 2=resta, 3=multiplicacion, 4=division")
operacion = int(input())
if operacion == 1:
    resultado = suma(n1, n2)
    print("La suma de sus numeros es: ", resultado)
elif operacion == 2:
    resultado = resta(n1, n2)
    print("La resta de sus numeros es: ", resultado)
elif operacion == 3:
    resultado = multiplicacion(n1, n2)
    print("La multiplicacion de sus numeros es: ", resultado)
elif operacion == 4:
    resultado = division(n1, n2)
    print("La division de sus numeros es: ", resultado)
else:
    print("Erorr!")
