#List <Can save different types of date>
lista = ["Josue Soto", "Josve", True, 1.63]
print(lista[0])
print(lista[1])
"""print(lista[2])
print(lista[3])"""

lista[0] = "Noe Soto"#Modifying the data in a list
print(lista[0])

#Tuples <Can save different types of date BUT the data can't be modified>
tupla = ("Noe Millan", "nikmilan", False, 21)
print(tupla[0])
print(tupla[1])
"""print(tupla[2])
print(tupla[3])"""

#Set / Conjunto, elements that are disordered and can change
#Does not allow repeating values or data, deletes it automatically
#We can't access through the index, it is through ALL the variable
#Se puede recorrer el set, PERO con un bucle
conjunto = {"Josue Soto", "Josve", True, 1.63}
print(conjunto)
conjunto={"Este es el conjunto editado ya que no podemos editarlo por índice"}
print(conjunto)

#Diccionario / dict, just like a list, but unordered
# "key" : "value"
"""
Son como libros mágicos
"""
diccionario = {
    "nombre": "jOSUE",
    "apellido": "sOTO",
    "edad": 23,
    "estatura": 1.63,
    "estado_animo" : True
    }
#print(diccionario)
print(diccionario["estado_animo"])#Imprimir el elemento "nombre" dentro de la variable diccionario
print(diccionario["estatura"]+.02)#We can do operations :d

###MIN 1:12:33