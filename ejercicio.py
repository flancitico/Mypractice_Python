n1 = int(input("Ingrese el primer número: "))
n2 = int(input("Ingrese el segundo número: "))
print("\n¿Qué operación desea realizar?")
print("Suma=1, Resta=2, Multiplicación=3, División=4")
operacion = int(input())

if operacion == 1:
    respuesta = n1 + n2
    print("Respuesta:", respuesta)
elif operacion == 2:
    respuesta = n1 - n2
    print("Respuesta:", respuesta)
elif operacion == 3:
    respuesta = n1 * n2
    print("Respuesta:", respuesta)
elif operacion == 4:
    if n2 != 0:  # Corrección: solo verificamos que n2 no sea 0
        respuesta = n1 / n2
        print("Respuesta:", respuesta)
    else:
        print("Error: No se puede dividir por cero.")
else:
    print("Operación no válida.")
