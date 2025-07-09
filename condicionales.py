# numero1 = int(input("ingrese el numero: "))

# if numero1 > 0:
#     print(f"es positivo porque es {numero1}")
# elif numero1 < 0:
#     print(f"es negativo porque es {numero1}")
# else:
#     print(f"es cero {numero1}")

#-------------------------------------------------------------------------------------
#calcula el mayor de dos numeros ingresados

# numero1 = int(input("ingrese un numero:"))
# numero2 = int(input("ingrese un numero:"))

# if numero1 > numero2:
#     print(f"{numero1} es mayor que {numero2}")
# elif numero1 < numero2:
#     print(f"{numero1} es menor que {numero2}")
# else:
#     print("son iguales")


#-------------------------------------ejercicios con condicionales---------------------------------------------------------------------------------
# 1. verifica si un numero es positivo, negativo o cero

# numero1 = int(input("ingrese el numero: "))

# if numero1 > 0:
#     print(f"es positivo porque es {numero1}")
# elif numero1 < 0:
#     print(f"es negativo porque es {numero1}")
# else:
#     print(f"es cero {numero1}")

#----------------------------------------------------------------------------------------------------------------------
# 2. calcula el mayor de dos numeros ingresados

# numero1 = int(input("ingrese un numero:"))
# numero2 = int(input("ingrese un numero:"))

# if numero1 > numero2:
#     print(f"{numero1} es mayor que {numero2}")
# elif numero1 < numero2:
#     print(f"{numero1} es menor que {numero2}")
# else:
#     print("son iguales")

#-----------------------------------------------------------------------------------------------------------------
# 3. determina si un numero es par o impar

# numero = int(input("ingresa un numero"))

# if numero % 2 == 0:
#     print(f"el numero {numero} es par")
# else:
#     print(f"el numero {numero} es impar")

#----------------------------------------------------------------------------------------------------------------------------
# 4. dado un numero verifica si esta entre 10 y 20

# numero = int(input("ingrese un numero:"))

# if numero <=9 or numero >=21:
#     print("el numero no esta entre 10 y 20")
# else:
#     print("el numero esta entre 10 y 20")

#--------------------------------------------------------------------------------------------------------------
# 5. dado tres numeros, encuentra el mayor usando condicionales

# numero1 = int(input("ingrese un numero:"))
# numero2 = int(input("ingrese un numero:"))
# numero3 = int(input("ingrese un numero:"))

# if numero1 > numero2 and numero3:
#     print(f"el numero {numero1} es el mayor")
# elif numero2 > numero3 and numero1:
#     print(f"el numero {numero2} es el mayor")
# else:
#     print(f"el numero {numero3} es el mayor")

#-------------------------------------------------------------------------------------------------------------
# 6. calcula el precio final con un 10% de descuento es mayor a 100.

# total = float(input("Ingresa el total de la compra: "))

# if total > 100:
#     descuento = total * 0.10
#     precio_final = total - descuento
#     print(f"Se aplica un 10% de descuento. Total a pagar: {precio_final}")
# else:
#     print(f"No se aplica descuento. Total a pagar: {total}")

#--------------------------------------------------------------------------------------------------------------------------------
# 7. verifica si una persona puede votar (mayor o igual a 18 años)

# edad = int(input("ingresa tu edad:"))

# if edad >=18:
#     print("puedes votar")
# else:
#     print("no puedes votar")

#----------------------------------------------------------------------------------------------------------------------------
# 8. dado el precio y tipo de cliente (vip o normal), aplica un descuento del 20% solo al vip

# precio = float(input("Ingresa el precio del producto: "))
# tipo_cliente = input("Ingresa el tipo de cliente (vip o normal): ")

# if tipo_cliente == "vip":
#     descuento = precio * 0.20
#     precio_final = precio - descuento
#     print(f"Cliente VIP: se aplica un 20% de descuento. Total a pagar: {precio_final:}")
# elif tipo_cliente == "normal":
#     print(f"Cliente normal: no se aplica descuento. Total a pagar: {precio:}")
# else:
#     print("Tipo de cliente no válido.")

#------------------------------------------------------------------------------------------------------------------------
# 9. determina si un numero es multiplo de 5 y de 3 al mismo tiempo

# numero = int(input("ingresa un numero:"))

# if numero % 5 == 0 and numero % 3 == 0:
#     print("el nuemro es multiplo de 5 y de 3 al mismo tiempo")
# elif numero % 5==0:
#     print("el numero solo es multiplo de 5")
# elif numero % 3==0:
#     print("el numero solo es multiplo de 3")
# else:
#     print("el numero no es multiplo ni de 5 ni de 3")


#-------------------------------------------------------------------------------------------------------------------------------------------
#10. dado un numero verifica si es divisible entre dos numeros dados

# numero = int(input("Ingresa el número principal: "))
# divisor1 = int(input("Ingresa el primer divisor: "))
# divisor2 = int(input("Ingresa el segundo divisor: "))

# if numero % divisor1 == 0 and numero % divisor2 == 0:
#     print(f"El número {numero} es divisible entre {divisor1} y {divisor2}.")
# else:
#     print(f"El número {numero} NO es divisible entre {divisor1} y {divisor2}.")


