#1. pide tu edad y muestra si eres menor de edad, mayor de edad o adulto mayor

# edad = int(input("ingresa tu edad: "))

# if edad <=17:
#     print(f"tienes {edad} años y eres menor de edad")
# elif edad >=18 and edad <=64:
#     print(f"tienes {edad} años y eres mayor de edad")
# else:
#     print(f"tienes {edad} años y eres un adulto mayor")


#----------------------------------------------------------------------------------------------------------------------------------
#2. solicita tu estatura en metros. si mide menos de 1.5 m, eres 
# considerado bajo; entre 1.5 y 1.8 m, estatura media; mas de 1.8 m, alto.

# altura = float(input("ingresa tu altura en metros (por ejemplo 1.6 ): "))

# if altura >0 and altura < 1.5:
#     print(f"tu altura es de {altura} m y eres considerado bajo")
# elif altura >= 1.5 and altura <= 1.8:
#     print(f"tu altura es de {altura} m y eres de estatura media")
# elif altura > 1.8:
#     print(f"tu altura es de {altura} m y eres considerado alto")
# else:
#     print("no dijitaste bien tu altura")

#---------------------------------------------------------------------------------------------------------------------------------
# 3. ingresa un numero y muestra si es multiplo de 2, de 3 o de ninguno

# numero = int(input("ingresa un numero: "))

# if numero % 2 == 0:
#     print(f"{numero} es multiplo de 2")
# elif numero % 3 == 0:
#     print(f"{numero} es multiplo de 3")
# elif numero % 2 == 0 and numero % 3 == 0:
#     print(f"{numero} es multiplo de 2 y de 3")
# else:
#     print(f"{numero} no es multiplo de 2 ni de 3")

#-----------------------------------------------------------------------------------------------------------------------------------
# 4. pide un numero decimal y determina si tiene 1,2 o mas de 2 decimales (usa str() y split())

# numero = float(input("ingresa un numero decimal: "))

# partes = str(numero).split('.')

# if len(partes) == 2:
#     decimales = partes[1]
#     cantidad_decimales = len(decimales)

#     if cantidad_decimales == 1:
#         print("El número tiene 1 decimal.")
#     elif cantidad_decimales == 2:
#         print("El número tiene 2 decimales.")
#     else:
#         print("El número tiene más de 2 decimales.")
# else:
#     print("El número no tiene parte decimal.")

#--------------------------------------------------------------------------------------------------------------------------------------------------------------
# 5 solicita un pais y muestra si esta en la siguiente tupla: ("colombia", "peru", "argentina", "mexico")

# tupla = ("colombia","peru","argentina","mexico")

# pais = input("ingresa un pais: ")

# if pais in tupla:
#     print(f"{pais} esta en la lista")
# else:
#     print(f"{pais} no esta en la lista")

#-----------------------------------------------------------------------------------------------------------------------------
# 6. pide tu tipo de sangre (A B AB, O) y muestra tu compatibilidad segun un diccionario predefinido

# compatibilidad = {
#     "O": ["O"],
#     "A": ["A", "O"],
#     "B": ["B", "O"],
#     "AB": ["A", "B", "AB", "O"]
# }

# tipo = input("Ingresa un tipo de sangre (A, B, AB, O): ").upper() #.upper es para si ingresa: b se convierta a B

# if tipo in compatibilidad:
#     compatibles = compatibilidad[tipo]
#     print(f"Un paciente con tipo de sangre {tipo} puede recibir sangre de: {(compatibles)}")
# else:
#     print("Tipo de sangre no válido. Debe ser A, B, AB o O.")

#-------------------------------------------------------------------------------------------------------------------
# 7. ingresa una temperatura en  °C si es menor de 10, hace frio. si esta entre 10 y 25 templado, mas de 25, hace calor.

# grados = int(input("ingresa un numero en °C: "))

# if grados < 10:
#     print("Hace frío.")
# elif 10 <= grados and grados <= 25:
#     print("Está templado.")
# else:
#     print("Hace calor.")

#------------------------------------------------------------------------------------------------------------------------------------------------
#8. crea un menu de opciones 1. sumar, 2, restar, 3. multiplicar. pide dos numeros y ejecuta la operacion seleccionada


# #menú de opciones
# print("Menú de operaciones:")
# print("1. Sumar")
# print("2. Restar")
# print("3. Multiplicar")

# # Pedir opcion al usuario
# opcion = input("Elige una opción (1, 2 o 3): ")

# # Verificar que la opcion sea válida
# if opcion in ("1", "2", "3"):
#     # Pedir dos números
#     num1 = float(input("Ingresa el primer número: "))
#     num2 = float(input("Ingresa el segundo número: "))

#     # Ejecutar la operacion seleccionada
#     if opcion == "1":
#         resultado = num1 + num2
#         print(f"La suma es: {resultado}")
#     elif opcion == "2":
#         resultado = num1 - num2
#         print(f"La resta es: {resultado}")
#     elif opcion == "3":
#         resultado = num1 * num2
#         print(f"La multiplicación es: {resultado}")
# else:
#     print("Opción no válida. Debes ingresar 1, 2 o 3.")

#----------------------------------------------------------------------------------------------------------------------------------------------
#9. pide un numero entre 1 y 12 y muestra el mes correspondiente usando un diccionario.

# Diccionario con los meses
# meses = {
#     1: "Enero",
#     2: "Febrero",
#     3: "Marzo",
#     4: "Abril",
#     5: "Mayo",
#     6: "Junio",
#     7: "Julio",
#     8: "Agosto",
#     9: "Septiembre",
#     10: "Octubre",
#     11: "Noviembre",
#     12: "Diciembre"
# }

# # Pedir un número entre 1 y 12
# numero = int(input("Ingresa un numero del 1 al 12: "))

# # Verificar si el número está en el diccionario
# if numero >= 1 and numero <= 12:
#     print(f"El mes correspondiente es: {meses[numero]}")
# else:
#     print("Error el numbero Debe estar entre 1 y 12.")

#---------------------------------------------------------------------------------------------------------------------------------
# #10.  solicita un numero de 4 digitos y determina si comienza con 1,2 o cualquier otro

# # Solicitar un número de 4 dígitos como cadena
# numero = input("Ingresa un número de 4 dígitos: ")

# # Verificar que tenga exactamente 4 dígitos y que sea numérico
# if len(numero) == 4 and numero:
#     primer_digito = numero[0]
    
#     if primer_digito == "1":
#         print("El número comienza con 1.")
#     elif primer_digito == "2":
#         print("El número comienza con 2.")
#     else:
#         print("El número comienza con otro dígito.")
# else:
#     print("Error Debes ingresar un número de 4 dígitos.")

#-------------------------------------------------------------------------------------------------------------------------------------
#11. ingresa una palabra. muestra si su primera letra es vocal, consonante o un numero

# palabra = input("Ingresa una palabra: ")

# if palabra:
#     primera = palabra[0].lower()  # se convierte en minuscula para que sea mas facil

#     # Listas de letras y números 
#     vocales = ['a', 'e', 'i', 'o', 'u']
#     letras = 'abcdefghijklmnopqrstuvwxyz'
#     numeros = '0123456789'

#     if primera in vocales:
#         print("La palabra comienza con una vocal.")
#     elif primera in letras:
#         print("La palabra comienza con una consonante.")
#     elif primera in numeros:
#         print("La palabra comienza con un número.")
# else:
#     print("No ingresaste ninguna palabra.")

#------------------------------------------------------------------------------------------------------------------------------
#12. pide una fruta si esta en la lista ["manzana","pera","piña"], muestra su precio. si no, indica que no esta disponible

# # Lista de frutas disponibles
# frutas = ["manzana", "pera", "piña"]

# # Lista de precios correspondientes (en el mismo orden)
# precios = [1.50, 1.20, 2.00]

# # Pedir una fruta al usuario
# fruta = input("Ingresa el nombre de una fruta: ").lower()

# # Verificar si la fruta está en la lista
# if fruta in frutas:
#     indice = frutas.index(fruta)
#     precio = precios[indice]
#     print(f"El precio de la {fruta} es {precio}")
# else:
#     print("esa fruta no está disponible.")

#---------------------------------------------------------------------------------------------------------------------------------
#13. pide tu calificacion (0 a 5). si es menor que 3, reprobado. entre 3 y 4, aprobado. mayor a 4, excelente

# calificacion = float(input("ingresa tu calificacion (de 0 a 5): "))

# if calificacion < 3:
#     print(f"tu nota es de {calificacion} y estas reprobado")
# elif calificacion >= 3 and calificacion <4:
#     print(f"tu nota es de {calificacion} y estas aproabado")
# elif calificacion >=4 and calificacion <=5:
#     print(f"tu nota es de {calificacion} y es excelente")
# else:
#     print("Nota no valida")

#--------------------------------------------------------------------------------------------------------------------------------
#14. pide un numero y muestra si es divisible entre 4, entre 6, o no lo es 

# numero = int(input("ingresa un numero: "))

# if numero % 4 == 0 and numero % 6 == 0:
#     print("El número es divisible entre 4 y 6.")
# elif numero % 4 == 0:
#     print("El número es divisible entre 4.")
# elif numero % 6 == 0:
#     print("El número es divisible entre 6.")
# else:
#     print("El número no es divisible ni entre 4 ni entre 6.")

#------------------------------------------------------------------------------------------------------------------------------
#15. crea un sistema de autenticacion basico pide usuaio y clave. Usa un diccionario para validar

# # Diccionario con usuarios y contraseñas
# usuarios = {
#     "juan": "123554",
#     "ana": "abcdef",
#     "maria": "clave2445"
# }

# # Solicitar usuario y contraseña
# usuario = input("Usuario: ").lower()
# clave = input("Clave: ")

# # Validar 
# if usuario in usuarios and clave == usuarios[usuario]:
#     print("Autenticación exitosa. ¡Bienvenido!")
# else:
#     print("Usuario o clave incorrectos.")

#--------------------------------------------------------------------------------------------------------------------------------------
#16. solicita una edad y muestra a que grupo pertenece: niño (0-12),
# # adolescente (13-17), adulto (18-64), mayor (65+).

# edad = int(input("ingresa tu edad: "))

# if edad >= 0 and edad <=12:
#     print(f"tienes {edad} años y perteneces al grupo : niño")
# elif edad >=13 and edad <=17:
#     print(f"tienes {edad} años y perteneces al grupo : adolescente")
# elif edad >= 18 and edad <=64:
#     print(f"tienes {edad} años y perteneces al grupo : adulto")
# else:
#     print(f"tienes {edad} años y perteneces al grupo : mayor")

#-------------------------------------------------------------------------------------------------------------------------------
#17. pide el nombre de una ciudad. si esta en una tupla, muestra que es capital; si no muestra "ciudad secundaria".

# # Tupla con nombres de capitales
# capitales = ("madrid", "paris", "londres", "berlin", "roma","bogota")

# # Pedir el nombre de una ciudad
# ciudad = input("Ingresa el nombre de una ciudad: ").lower()

# # Verificar si es una capital
# if ciudad in capitales:
#     print(f"{ciudad} es una capital.")
# else:
#     print(f"{ciudad} es una ciudad secundaria.")

#------------------------------------------------------------------------------------------------------------------------------
#18. ingresa el valor de una compra. si es mayor de $200.000 aplica un 15% de descuento entre $100.000 y $200.000 aplica 10%. si es menor, no hay descuento.

# # Pedir el valor de la compra
# valor = float(input("Ingresa el valor de la compra: $"))

# # Calcular descuento según el valor
# if valor > 200000:
#     descuento = valor * 0.15
# elif 100000 <= valor <= 200000:
#     descuento = valor * 0.10
# else:
#     descuento = 0

# # Calcular precio final
# total = valor - descuento

# # Mostrar resultados
# print(f"Descuento aplicado: ${descuento}")
# print(f"Total a pagar: ${total}")

#------------------------------------------------------------------------------------------------------------------------------------
# 19. pide el nombre y el numero de horas trabajadas calcula el salario con tarifa de $10.000/hora. si trabajo mas de 40 horas, aplica un bono del 20%

# # Solicitar datos
# nombre = input("Ingresa tu nombre: ")
# horas = float(input("Número de horas trabajadas: "))

# # Tarifa por hora
# tarifa = 10000

# # Calcular salario base
# salario = horas * tarifa

# # Aplicar bono si trabajó más de 40 horas
# if horas > 40:
#     bono = salario * 0.20
# else:
#     bono = 0

# # Salario total
# salario_total = salario + bono

# # Mostrar resultados
# print(f"\nEmpleado: {nombre}")
# print(f"Salario base: ${salario}")
# print(f"Bono: ${bono}")
# print(f"Salario total a pagar: ${salario_total}")

#-------------------------------------------------------------------------------------------------------------------------------
#20. ingresa tu puntaje en una prueba(0 a 100). si es menor a 50, insuficiente. De 50 a 79, aceptable. 80 a 100, sobresaliente

# # Pedir puntaje
# puntaje = int(input("Ingresa tu puntaje en la prueba (0 a 100): "))

# # Validar y mostrar resultado
# if 0 <= puntaje < 50:
#     print("Insuficiente")
# elif 50 <= puntaje <= 79:
#     print("Aceptable")
# elif 80 <= puntaje <= 100:
#     print("Sobresaliente")
# else:
#     print("Puntaje no válido. Debe estar entre 0 y 100.")








