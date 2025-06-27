numeros = []

numero1 = int(input("añade un numero: "))
numero2 = int(input("añade un numero: "))
numero3 = int(input("añade un numero: "))
numero4 = int(input("añade un numero: "))

numeros.append(numero1)
numeros.append(numero2)
numeros.append(numero3)
numeros.append(numero4)

print(f"la lista es: {numeros}")
print("El numero mayor es:", max(numeros))
print("El numero menor es:", min(numeros))


