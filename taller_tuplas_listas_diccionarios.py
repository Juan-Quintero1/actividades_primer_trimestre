#ejercicio de practica

#----------------------------calculadora promedio-----------------------------------------------------------------------------

# lista = []

# calificacion1 = float(input("ingrese la calificacion:"))
# calificacion2 = float(input("ingrese la calificacion:"))
# calificacion3 = float(input("ingrese la calificacion:"))

# lista.append(calificacion1)
# lista.append(calificacion2)
# lista.append(calificacion3)

# cantidad_numeros = float(input("ingrese la cantidad de numeros: "))
# promedio = (calificacion1 + calificacion2 + calificacion3)/(cantidad_numeros)

# print(f"las calificaciones son {lista}, y el promedio de estas es {promedio}")

#------------------------------actualizacion-------------------------------------------------------------------

# productos={
# "pan":3.500,
# "leche":2.300,
# "huevos":1.500,
# }
# print(productos)
# porcentaje_aumento = float(input("Porcentaje de aumento %: "))
# productos["pan"]+=productos["pan"] * (porcentaje_aumento/100)
# productos["leche"]+=productos["leche"] * (porcentaje_aumento/100)
# productos["huevos"]+=productos["huevos"] * (porcentaje_aumento/100)

# print(productos)

#-----------------------------conversor de temperatura--------------------------------------------------------------------------------

# temp_celcius = (18.5,20.0,19.3,22.1,21.3)
# print(temp_celcius)

# t1 = (temp_celcius[0] * 9/5) + 32
# t2 = (temp_celcius[1] * 9/5) + 32
# t3 = (temp_celcius[2] * 9/5) + 32
# t4 = (temp_celcius[3] * 9/5) + 32
# t5 = (temp_celcius[4] * 9/5) + 32

# temp_fahrenheit = (t1,t2,t3,t4,t5)
# print(temp_fahrenheit)

#-----------------------------edad promedio con listas-----------------------------------------------------------------------------------------

# edades = []

# e1 = int(input("ingrese la edad: "))
# e2 = int(input("ingrese la edad: "))
# e3 = int(input("ingrese la edad: "))
# e4 = int(input("ingrese la edad: "))
# e5 = int(input("ingrese la edad: "))

# edades.append(e1)
# edades.append(e2)
# edades.append(e3)
# edades.append(e4)
# edades.append(e5)

# cantidad_edades = float(input("ingrese la cantidad de edades: "))
# promedio = (e1 + e2 + e3 + e4 + e5)/(cantidad_edades)

# print(f"la lista de edades es {edades} el mayor es {max(edades)},el menor es menor{min(edades)}, y el promedio de las edades es{promedio}")

#--------------------------------------diccionario de frutas--------------------------------------------------------------------------------------

# frutas={
#     "pera": 1500,
#     "manzana": 2500,
#     "uva": 3000
# }

# kilos_pera = float(input("cuantos kilos de pera necesita:"))
# kilos_manzana = float(input("cuantos kilos de manzana necesita:"))
# kilos_uva = float(input("cuantos kilos de uva necesita:"))

# total = (
#     kilos_pera * frutas["pera"]+
#     kilos_manzana * frutas["manzana"]+
#     kilos_uva * frutas["uva"]
# )

# print(f"\nTotal a pagar: {total:} COP") # codigo

#-----------------------------------suma de elementos en tupla-------------------------------------------------------------------

# numeros = (4, 7, 2, 9, 5)

# suma_total = sum(numeros)

# print("La suma total de los numeros es:", suma_total)

#-----------------------------------inventario con lista de diccionarios--------------------------------------------------------------

# producto1 = {
#     "nombre": input("Nombre del producto 1: "),
#     "cantidad": int(input("Cantidad: ")),
#     "precio": float(input("Precio unitario: "))
# }

# producto2 = {
#     "nombre": input("Nombre del producto 2: "),
#     "cantidad": int(input("Cantidad: ")),
#     "precio": float(input("Precio unitario: "))
# }

# producto3 = {
#     "nombre": input("Nombre del producto 3: "),
#     "cantidad": int(input("Cantidad: ")),
#     "precio": float(input("Precio unitario: "))
# }

# total = (
#     producto1["cantidad"] * producto1["precio"] +
#     producto2["cantidad"] * producto2["precio"] +
#     producto3["cantidad"] * producto3["precio"]
# )

# print(f"El total del inventario es: {total}")

#-------------------------------------------------modificar una lista de precios----------------------------------------------------------------

# precios = [1800, 2500, 7500, 1800, 6000]

# descuento = float(input("Ingresa el descuento: "))
# descuento_ = descuento / 100

# precio1 = precios[0] - (precios[0] * descuento_)
# precio2 = precios[1] - (precios[1] * descuento_)
# precio3 = precios[2] - (precios[2] * descuento_)
# precio4 = precios[3] - (precios[3] * descuento_)
# precio5 = precios[4] - (precios[4] * descuento_)

# precios_con_descuento = [precio1, precio2, precio3, precio4, precio5]

# print("Precios con descuento asignado:")
# print(precios_con_descuento)

#---------------------------------------Notas con tupla---------------------------------------------------------

# notas_lista = []
# n1 = float(input("Ingresa la nota 1: "))
# n2 = float(input("Ingresa la nota 2: "))
# n3 = float(input("Ingresa la nota 3: "))
# n4 = float(input("Ingresa la nota 4: "))

# notas = (n1, n2, n3, n4)

# nota_mayor = max(notas)
# nota_menor = min(notas)

# print(f"\nNota más alta: {nota_mayor}")
# print(f"Nota más baja: {nota_menor}")

#----------------------------------------------diccionario de conversiones------------------------------------------------------------------

# equivalencias = {
#     "km": 1000,
#     "m": 1,
#     "cm": 0.01
# }

# cantidad = float(input("Ingresa la cantidad: "))
# unidad = input("Ingresa la unidad (km, m, cm): ")

# metros = cantidad * equivalencias.get(unidad,0)

# if metros == 0:
#     print("Unidad no válida.")
# else:
#     print(f"{cantidad} {unidad} equivalen a {metros} metros.")

#-----------------------------------------lista de productos mas iva-------------------------------------------------------------------

# precios_str = input("Ingresa una lista de precios separados por comas: ")
# precios = [float(p) for p in precios_str.split(",")]

# iva = 0.19
# precios_con_iva = [p * (1 + iva) for p in precios]

# print("Precios con IVA incluido:")
# print(precios_con_iva)

#-----------------------------------------------tuplas de operaciones matematicas-------------------------------------------------------

# num1 = float(input("Ingresa el primer número: "))
# num2 = float(input("Ingresa el segundo número: "))

# suma = num1 + num2
# resta = num1 - num2
# multiplicacion = num1 * num2
# division = num1 / num2  # Asume que num2 != 0

# resultados = (suma, resta, multiplicacion, division)

# print("Resultados (suma, resta, multiplicación, división):")
# print(resultados)

#------------------------------------------diccionario de estudiantes--------------------------------------------------------------------------------------------

# notas_estudiantes = {
#     "Ana": 8.5,
#     "Luis": 7.2,
#     "María": 9.1,
#     "Carlos": 6.8,
#     "Sofía": 8.0
# }

# suma_notas = sum(notas_estudiantes.values())

# promedio = suma_notas / len(notas_estudiantes)

# print(f"El promedio general es: {promedio}")

#------------------------------------lista de salarios---------------------------------------------------------------------

# salarios = []

# for i in range(5):
#     salario = float(input(f"Ingresa el salario {i + 1}: "))
#     salarios.append(salario)

# aumento = 0.10
# salarios_actualizados = [salario * (1 + aumento) for salario in salarios]

# print("\nSalarios con aumento del 10%:")
# print(salarios_actualizados)

#----------------------------------------diccionario de impuestos----------------------------------------------------------------------------------------

# productos = {
#     "manzana": 1.500,
#     "pan": 2.200,
#     "leche": 3.00,
#     "huevos": 4.200,
#     "arroz": 3.200
# }

# impuesto = float(input("Ingresa el porcentaje de impuesto: "))
# impuesto_ = impuesto / 100

# print("\nPrecios con impuesto aplicado:")
# for producto, precio in productos.items():
#     precio_final = precio * (1 + impuesto_)
#     print(f"{producto}: {precio_final}")

#----------------------------------------analisis de lista de edades--------------------------------------------------------------------------

# edades_str = input("Ingresa una lista de edades separadas por comas: ")
# edades = [int(e.strip()) for e in edades_str.split(",")]

# mayores = sum(1 for edad in edades if edad >= 18)
# menores = len(edades) - mayores

# print(f"\nCantidad de mayores de edad: {mayores}")
# print(f"Cantidad de menores de edad: {menores}")

#---------------------------------------------tupla de conversion de moneda----------------------------------------------------------

# tasa_euro = 0.92         
# tasa_peso_col = 4900     
# tasa_yen = 135           

# cantidad_usd = float(input("Ingresa la cantidad en dólares USD: "))

# euros = cantidad_usd * tasa_euro
# pesos_col = cantidad_usd * tasa_peso_col
# yenes = cantidad_usd * tasa_yen

# conversiones = (euros, pesos_col, yenes)

# print(f"\nEquivalencias para ${cantidad_usd} USD:")
# print(f"Euros: {euros} EUR")
# print(f"Pesos Colombianos: {pesos_col} COP")
# print(f"Yenes: {yenes} JPY")

#------------------------------------------diccionario de ventas-------------------------------------------------------------------

# ventas = {}

# for i in range(3):
#     nombre = input(f"Nombre del producto {i+1}: ")
#     cantidad = int(input(f"Cantidad vendida de {nombre}: "))
#     ventas[nombre] = cantidad

# total_unidades = sum(ventas.values())

# print(f"Total de unidades vendidas: {total_unidades}")
# print(ventas)

#-----------------------------------lista de temperaturas extremas---------------------------------------------------------------------------

# temperaturas = [12, 35, 28, 9, 31, 7, 15, 40, 3, 25]

# mayores_30 = [t for t in temperaturas if t > 30]
# menores_10 = [t for t in temperaturas if t < 10]

# print("Temperaturas mayores a 30°C:", mayores_30)
# print("Temperaturas menores a 10°C:", menores_10)

#-----------------------------------actualizar precios con metodos listas--------------------------------------------------------------------------------

# precios = [100.0, 250.0, 75.0, 180.0, 60.0]

# precio_eliminar = float(input("Ingresa el precio que deseas eliminar de la lista: "))
# if precio_eliminar in precios:
#     precios.remove(precio_eliminar)
# else:
#     print("Ese precio no está en la lista.")

# nuevo_precio = float(input("Ingresa un nuevo precio para agregar: "))
# precios.append(nuevo_precio)

# precios_ordenados = sorted(precios)

# print("\nLista ordenada de precios:")
# print(precios_ordenados)

