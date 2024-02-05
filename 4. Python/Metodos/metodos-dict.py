"""
Son como libros mágicos, los métodos ayudan a interactuar con esta clase de datos compuestos
"""

diccionario = {
    "nombre" : "Las aventuras de Abbi",
    "apellido" : "López",
    "cost" : 500000
}

#claves = diccionario.keys()
#claves = diccionario.get("cost")
#claves = diccionario.clear()
#claves = diccionario.pop("cost")
claves = diccionario.items()
print(claves)
#print(diccionario)

#Podemos usar esa manera de revisar los diccionarios, pero no son listas, así que es recomendable usar get
#print(diccionario["nombre"])

"""
keys() - devuelve las claves / También podemos iterar /  devuelve un objeto de tipo dict_item que se puede iterar
get()- devuelve el valor de una clave / si hay un error, el programa no se detiene, continua
pop() - elimina un elemento
items() - para iterar el dict / También podemos iterar / este es el bueno para iterar porque nos da un método dict_items
"""