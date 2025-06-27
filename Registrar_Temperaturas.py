temperaturas = []

temperatura_celsius1 = int(input("ingrese una temeperatura:"))
temperatura_celsius2 = int(input("ingrese una temeperatura:"))

temperaturas.append(temperatura_celsius1)
temperaturas.append(temperatura_celsius2)

fahrenheit = (temperaturas * 9/5) + 32

print(fahrenheit)