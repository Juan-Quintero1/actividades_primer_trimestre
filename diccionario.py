auto = {
"marca":"ford",
"modelo":"mustang",
"año":2025,
"color":"rojo",

}

#acceder al modelo

# print(auto["modelo"])

#modificar

auto["año"] = 2023

#añadir nuevo elemento

auto["color"] ="verde"

# print(auto)

#ELIMINAR ELEMENTOS

del auto["modelo"]
print(auto)

auto.pop("marca")
print(auto)