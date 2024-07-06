palabra = " "
vocales = 0
palabra = input("Ingresa una palabra: ").lower()
for i in range(len(palabra)):
    if palabra[i] in "aeiou":
        vocales += 1
print(f"La cantidad de vocales de {palabra} es {vocales}")
