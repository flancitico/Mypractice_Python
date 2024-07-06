def factorial(numero):
    multiplicacion = 1
    for i in range(1, numero+1):
        multiplicacion *= i
    return multiplicacion


numero = int(input("Ingrese un numero: "))
resultado = factorial(numero)
print(f"El resultado del {numero}, su factorial es: {resultado} ")
