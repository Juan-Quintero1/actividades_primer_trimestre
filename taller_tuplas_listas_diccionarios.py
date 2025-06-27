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

frutas={
    "pera": 1500,
    "manzana": 2500,
    "uva": 3000
}

kilos_pera = float(input("cuantos kilos de pera necesita:"))
kilos_manzana = float(input("cuantos kilos de manzana necesita:"))
kilos_uva = float(input("cuantos kilos de uva necesita:"))

total = (
    kilos_pera * frutas["pera"]+
    kilos_manzana * frutas["manzana"]+
    kilos_uva * frutas["uva"]
)

print(f"\nTotal a pagar: {total:} COP") # codigooooooooo

#-----------------------------------suma de elementos en tupla-------------------------------------------------------------------

