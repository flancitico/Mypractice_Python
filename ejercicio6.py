numero = int(input("Ingresa un numero: "))
pares = []
impares = []
for i in range(1, numero+1):
    if i % 2 == 0:
        pares.append(i)
    else:
        impares.append(i)
print("Numeros pares: ", pares)
print("Numeros impares: ", impares)
