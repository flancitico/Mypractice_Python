cantidad = int(input("¿Cuántos números desea ingresar? "))
numeros = []

for i in range(cantidad):  # Corrige la sintaxis del bucle for
    numero = float(input(f"Ingrese el número {i+1}: "))
    numeros.append(numero)

# Calcula el promedio sumando todos los números y dividiendo por la cantidad
suma = sum(numeros)
respuesta = suma / cantidad

print("Respuesta del promedio:", respuesta)
