import random
numerorandom = random.randint(1, 100)
print("Adivina el numero!")
numerousuario = int(input("\nIngresa el numero que pienses que sea: "))
intentos = 1
while numerousuario != numerorandom:
    if numerousuario < numerorandom:
        print("\n Incorrecto!")
        print("\nPista: EL numero es mayor")
    elif numerousuario > numerorandom:
        print("\nIncorrecto!")
        print("\nPista: El numero es menor")
    numerousuario = int(input("\nIntentalo de nuevo: "))
    intentos += 1

print("Correcto el numero a advinar es: ", numerorandom)
print("\nTu numero de intentos fue: ", intentos)
