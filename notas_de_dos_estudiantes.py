notas = []

nota1 = float(input("ingresa la nota: "))
nota2 = float(input("ingresa la nota: "))

notas.append(nota1)
notas.append(nota2)

cantidad_de_notas = int(input("ingrese la cantidad de notas"))
promedio = (nota1 + nota2)/(cantidad_de_notas)

print(f"estas son las notas {notas}, y el promedio de estas es {promedio}")
