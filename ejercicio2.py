def nPrimo(n):
    if (n <= 1):
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True


n = int(input("Ingresa un numero para verificar si es primo o no: "))
if nPrimo(n):
    print("El numero es primo")
else:
    print("El numero no es primo")
