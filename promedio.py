#de manera individual desarrolla un programa que permita calcura el promedio final de puntos de los equipos de futbol en un torneo

equipo1 = input("ingrese el nonbre del equipo: ")
equipo2 = input("ingrese el nonbre del equipo: ")
equipo3 = input("ingrese el nonbre del equipo: ")

puntos1 = int(input(f"ingrese los puntos finales del {equipo1} : "))
puntos2 = int(input(f"ingrese los puntos finales del {equipo2} : "))
puntos3 = int(input(f"ingrese los puntos finales del {equipo3} : "))

cantidad_de_equipos = int(input("ingrese cuantos equipos participaron: "))

promedio = (puntos1 + puntos2 + puntos3)/(cantidad_de_equipos)

print(f"el promedio de los puntos del partido de los equipos es {promedio}")