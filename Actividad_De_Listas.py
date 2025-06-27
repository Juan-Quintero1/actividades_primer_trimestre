LISTA1 = [100,"hola mundo"]
LISTA2 = ["Hola y Adios",300]

LISTA3 = LISTA1.copy()
LISTA3.pop()
#print(LISTA3)

LISTA4 =LISTA2.copy()
LISTA4.pop()
LISTA4.pop(0)
#print(LISTA4)

LISTA5 = LISTA4.copy()
LISTA5.extend(LISTA3)

print(LISTA5)