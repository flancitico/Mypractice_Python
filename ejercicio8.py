numeros = []
entrada = input("Ingrese numeros: ")
numeros = [int(x) for x in entrada.split()]
for i in range(len(numeros)):

    print(numeros[i])
