precios = []

precio1 = float(input("añade un precio: "))
precio2 = float(input("añade un precio: "))
precio3 = float(input("añade un precio: "))

precios.append(precio1)
precios.append(precio2)
precios.append(precio3)

print(precios)

precios_total = (precio1 + precio2 + precio3)

print(f"el precio total es de: {precios_total}")
