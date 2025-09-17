"""
##### listas ####


producti = "lata de atun"

lista_productos = ["choclo", "lata de atun", "manzana"] # puden ser diferente tipos de datos

print(lista_productos) 


tupla_productos = ("durazno", "manzana") # no se puede modificar


lista_productos.append("naranja")

print(lista_productos) 
print(len(lista_productos))

lista_productos.pop()  #metodo pop elimina el  ultimo elemento de la lista

print(lista_productos)

print(len(lista_productos))
"""


### dictionarios------------ se escriben en formato JSON



"""
persona = {
    "nombre" : "jose",
    "apellido": "montezuma",
    "edad": 23,
    "licencia_conducir": False
}


persona["email"] = "jose@gmail.com"
print(persona)

"""


#funciones

def suma(a , b ):
    result = a+b
    return result , a

def resta(a , b ):
    result = a-b
    return result


resultado_suma = suma(2 , 5 )
resultado_resta = resta (1 , 3)

print(resultado_suma)
print(resultado_resta)